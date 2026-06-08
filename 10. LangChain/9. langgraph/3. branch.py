import uuid

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, BaseMessage
from langchain_core.runnables import RunnableConfig

from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.checkpoint.memory import MemorySaver

from typing import TypedDict, List, Dict, Any

load_dotenv()

# class State(TypedDict):
#     messages: List[AIMessage]
#     topic: str
class State(TypedDict):
    messages: List[BaseMessage]
    topic: str

llm = ChatOpenAI(model='gpt-4o-mini')
# graph = StateGraph(state_schema=MessagesState)
graph = StateGraph(State)
memory = MemorySaver()

# ┌─────────┐
# │  START  │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐
# │ router  │
# └────┬────┘
#      │
#      │ topic_router()
#      │
#  ┌───┼───────────────┐
#  │   │               │
#  ▼   ▼               ▼
# weather          news          chat
#  │                │             │
#  ▼                ▼             ▼
# END              END           END

def get_weather(): return '오늘 서울의 날씨는 맑고 기온의 22도입니다'
def get_news(): return '최신 뉴스: 오늘 삼성전자의 주가는 -9% 하락중입니다'

def topic_router(state: State, config: RunnableConfig) -> str:
    '''사용자 질문에 따라 경로를 라우팅'''
    last_message = state['messages'][-1].content.lower()

    if '날씨' in last_message:
        print('[ROUTER] weather routing . . .')
        return 'weather'
    
    if '뉴스' in last_message:
        print('[ROUTER] news routing . . .')
        return 'news'
    
    print('[ROUTER] chat routing . . .')
    return 'chat'

def router_node(state: State, config: RunnableConfig) -> Dict[str, Any]:
    return state

def weather_node(state: State, config: RunnableConfig) -> Dict[str, Any]:
    weather_info = get_weather()
    res = llm.invoke([
        SystemMessage(content='당신은 날씨 전문가'),
        HumanMessage(content=f'다음 날씨 정보를 사용자에게 전달: {weather_info}')
    ])
    return {'messages': state['messages'] + [res], 'topic': 'weather'}

def news_node(state: State, config: RunnableConfig) -> Dict[str, Any]:
    news_info = get_news()
    res = llm.invoke([
        SystemMessage(content='당신은 뉴스 전문가'),
        HumanMessage(content=f'다음 뉴스 정보를 사용자에게 전달: {news_info}')
    ])
    return {'messages': state['messages'] + [res], 'topic': 'news'}

def chat_node(state: State, config: RunnableConfig) -> Dict[str, Any]:
    messages = state['messages']
    res = llm.invoke([
        SystemMessage(content='당신은 AI 비서'),
        HumanMessage(content=f'{messages}')
    ])
    return {'messages': state['messages'] + [res], 'topic': 'chat'}

graph.add_node('router', router_node)
graph.add_node('weather', weather_node)
graph.add_node('news', news_node)
graph.add_node('chat', chat_node)

graph.add_edge(START, 'router')
graph.add_conditional_edges(
    'router', topic_router,
    path_map={
        'weather': 'weather',
        'news': 'news',
        'chat': 'chat'
    }
)

graph.add_edge('weather', END)
graph.add_edge('news', END)
graph.add_edge('chat', END)

app = graph.compile(checkpointer=memory)
thread_id = str(uuid.uuid4())
config = {'configurable': {'thread_id': thread_id}}

while True:
    user_input = input('Enter a question: ')
    if user_input.lower() == 'exit':
        break

    result = app.invoke({
        'messages': [HumanMessage(content=user_input)],
        'topic': ''
    }, config=config)
    print(f'[AI RESPONSE] [{result["topic"]}] {result["messages"][-1].content}')