from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()
checkpoint = MemorySaver()

@tool
def send_payment(recipient: str, amount: int) -> str:
    '''수신자에게 지정 금액을 송금'''
    return f'{recipient}에게 {amount}원 송금 완료'

llm = ChatOpenAI(model='gpt-4o-mini')
agent = create_agent(
    llm, [send_payment], 
    checkpointer=checkpoint, 
    interrupt_before=['tools'])

config = {'configurable': {'thread_id': 't001'}}
question = '홍길동에게 십만원 송금'

print(f'[USER] {question}')
result = agent.invoke({'messages': [('user', question)]}, config=config)

call = result['messages'][-1].tool_calls[0] # stop point -> before calling the tool
print(f'[PAUSE] {call['name']} ({call['args']})')

human_result = input('Do you send money? (y/n)\n').strip().lower()
if human_result == 'y':
    result = agent.invoke(None, config=config)
    print(f'[RESULT] {result['messages'][-1].content}')
elif human_result == 'n':
    print(f'[STOP] This work is stopped by client request')