from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

from pprint import pprint

load_dotenv()
checkpoint = MemorySaver()
accounts = {
    'alice': 1_000_000,
    'bob': 500_000
}

@tool
def send_payment(recipient: str, amount: int) -> str:
    '''Remittance of a specified amount to the recipient'''
    accounts['alice'] -= amount
    accounts[recipient] += amount
    return f'{recipient}에게 {amount}원 송금 완료'

@tool
def get_balance(account: str) -> int:
    '''View balance of client's account'''
    return accounts.get(account, 0)

llm = ChatOpenAI(model='gpt-4o-mini')
agent = create_agent(
    llm, [send_payment, get_balance], 
    checkpointer=checkpoint, 
    interrupt_before=['tools'])

config = {'configurable': {'thread_id': 't001'}}
questions = [
    'alice의 잔액은 얼마야',
    'alice가 bob에게 십만원 송금',
    'alice와 bob의 잔액을 조회'
]

for question in questions:
    print(f'[USER] {question}')
    result = agent.invoke({'messages': [('user', question)]}, config=config)

    while True:
        last_msg = result['messages'][-1]
        if not getattr(last_msg, "tool_calls", None): break
        for call in last_msg.tool_calls:
            print(f"[PAUSE] {call['name']} ({call['args']})")

        # 송금이 아니면 계속하도록
        if last_msg.tool_calls[0]['name'] != 'send_payment':
            result = agent.invoke(None, config=config)
            continue

        human_result = input('Do you send money? (y/n) ').strip().lower()
        if human_result == 'y':
            result = agent.invoke(None, config=config)
            print(f'[RESULT] {result['messages'][-1].content}')
        elif human_result == 'n':
            print(f'[STOP] This work is stopped by client request')
            break
    print(f"[RESULT] {result['messages'][-1].content}")