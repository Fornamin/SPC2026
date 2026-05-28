import os
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI

openai_api_key = os.environ.get('OPEN_API_KEY')
lim = OpenAI(model='gpt-4o-mini')

prompt = '다음 말을 한국어로 번역해줘: i want to sleep'
print(lim.invoke(prompt))

lim2 = ChatOpenAI(model='gpt-4o-mini')
prompt2 = '게임 회사를 창업하려고 하는데 이름 후보군을 3개 지어줘'
print(lim.invoke(prompt2))

from langchain_core.messages import SystemMessage, HumanMessage
prompt3 = [
    SystemMessage(content='당신은 창의력이 높은 작명가입니다'),
    HumanMessage(content='게임 회사를 창업하려고 하는데 이름 후보군을 3개 지어줘')
]
print(lim.invoke(prompt3))