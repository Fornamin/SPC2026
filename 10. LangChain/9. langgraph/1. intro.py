from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()
llm = ChatOpenAI(model='gpt-4o-mini')

#             엣지(edge)   노드(node)   엣지(edge)
# 그래프 구조 : [ START ] -> [ model ] -> [ END ]
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

app = graph.compile()

user_input = input('\nEnter a Question: ')
result = app.invoke({'messages': [HumanMessage(content=user_input)]})

for i, message in enumerate(result['messages']):
    print(f'Message {i}\n[{message.type.upper()}]: {message.content}')