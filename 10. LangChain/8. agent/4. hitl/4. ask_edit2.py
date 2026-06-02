from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.messages import AIMessage
from langgraph.checkpoint.memory import MemorySaver

from pprint import pprint

load_dotenv()
checkpoint = MemorySaver()

@tool
def send_payment(recipient: str, amount: int) -> str:
    '''Remittance of a specified amount to the recipient'''
    return f'{recipient}에게 {amount}원 송금 완료'

@tool
def get_balance(account: str) -> int:
    '''View balance of client's account'''
    return {'alice': 1_000_000, 'bob': 500_000}.get(account, 0)

llm = ChatOpenAI(model='gpt-4o-mini')
agent = create_agent(
    llm, [send_payment, get_balance], 
    checkpointer=checkpoint, 
    interrupt_before=['tools'])

config = {'configurable': {'thread_id': 't001'}}
question = 'bob에게 만원을 송금'
print(f'[QUESTION] {question}')
result = agent.invoke({"messages": [("user", question)]}, config=config)

# 1. 현재 멈춰 있는 상태 조회
ai_msg = agent.get_state(config).values['messages'][-1]
call = ai_msg.tool_calls[0]
args = call['args']
print(f'[Agent Suggestion] {call['name']} ({call['args']})')

# 2. 해당 상태를 사용자가 수동으로 수정
print(f'Do you send money to {args['recipient']}?')
print(' 1. yes')
print(' 2. no')
print(' 3. change amount of money')
choice = input('Choice (1/2/3): ')

if choice == '2':
    print('[CANCLED] cancled by client request')
else:
    if choice == '3':
        new_amount = int(input('Enter a new amount of money: ').strip())
        edited = {**call, 'args': {**call['args'], 'amount': new_amount}}

        fixed = AIMessage(content=ai_msg.content, tool_calls=[edited], id=ai_msg.id)
        agent.update_state(config, {'messages': [fixed]})
        print(f'[UPDATED] {new_amount} krw')

    result = agent.invoke(None, config=config)
    final = result['messages'][-1].content

    if not final:
        final = result['messages'][-2].content
    print(f'[RESULT] {final}')