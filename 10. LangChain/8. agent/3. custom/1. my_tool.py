from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str: # 매개변수는 str이며 str을 반환
    '''calculate mathematical expressions ex. 5 + 8 / 2 = 9'''
    try:
        return str(eval(expression, {'__builtins__': {}}, {})) # 내부 built-in 함수들의 호출을 금지
    except Exception as e:
        return f'Calculation Error: {e}'
    
llm = ChatOpenAI(model='gpt-4o-mini')
agent = create_agent(llm, [calculator])
result = agent.invoke({
    'messages': [('user', '10 나누기 2 곱하기 5는?')]
})

print(result['messages'][-1].content)