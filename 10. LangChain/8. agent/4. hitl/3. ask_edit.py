from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.messages import AIMessage
from langgraph.checkpoint.memory import MemorySaver

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

print(f'[Agent Suggestion] {call['name']} ({call['args']})')

# 2. 해당 상태를 사용자가 수동으로 수정
edited = {**call, 'args': {**call['args'], 'amount': 5000}}
fixed = AIMessage(content=ai_msg.content, tool_calls=[edited], id=ai_msg.id)
agent.update_state(config, {'messages': [fixed]})

# 3. 다시 이어서 실행
result = agent.invoke(None, config=config)
print(f'[RESULT] {result}')