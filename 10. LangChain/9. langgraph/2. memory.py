import uuid

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')
memory = MemorySaver()

#             엣지(edge)   노드(node)   엣지(edge)
# 그래프 구조 : [ START ] -> [ model ] -> [ END ]
#                            ^ Memory Saver

graph = StateGraph(state_schema=MessagesState)

def call_model(state):
    messages = state['messages']
    system_message = SystemMessage(content='당신은 친절한 AI 비서')
    all_messages = [system_message] + messages

    print('Executing Model Fuction . . . / Length of Messages', len(messages))
    res = llm.invoke(all_messages)
    print('Completed Generating Model Response: ', res.content[:50])

    return {'messages': res}

graph.add_node('model', call_model)
graph.add_edge(START, 'model')
graph.add_edge('model', END)

app = graph.compile(checkpointer=memory)

thread_id_x = str(uuid.uuid4())
config_x = {'configurable': {'thread_id': thread_id_x}}

result = app.invoke({
    'messages': [HumanMessage(content='안녕하세요 제 이름은 김철수입니다')]}, config=config_x)
print(f'[AI RESPONSE] {result['messages'][-1].content}')
result = app.invoke({
    'messages': [HumanMessage(content='제 이름이 무엇일까요')]}, config=config_x)
print(f'[AI RESPONSE] {result['messages'][-1].content}')

thread_id_y = str(uuid.uuid4())
config_y = {'configurable': {'thread_id': thread_id_y}}

result = app.invoke({
    'messages': [HumanMessage(content='안녕하세요 제 이름은 김영희입니다')]}, config=config_y)
print(f'[AI RESPONSE] {result['messages'][-1].content}')
result = app.invoke({
    'messages': [HumanMessage(content='제 이름이 무엇일까요')]}, config=config_y)
print(f'[AI RESPONSE] {result['messages'][-1].content}')