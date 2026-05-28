import os
from dotenv import load_dotenv

load_dotenv()

from langchain_openai import OpenAI      # 단발성 질문 (Instruct Model = gpt-3.5-turbo-instruct)
from langchain_openai import ChatOpenAI  # Q&A 용으로 사용 (Chat Model = gpt-3.5-turbo)

openai_api_key = os.environ.get('OPEN_API_KEY')
llm = OpenAI(model='gpt-4o-mini')

prompt = '다음 말을 한국어로 번역해줘: An apple is on the chair.'
print(llm.invoke(prompt))
print('-' * 100)

llm2 = ChatOpenAI(model='gpt-4o-mini')
prompt2 = '게임 회사를 창업하려고 하는데 이름 후보군을 3개 지어줘'
result = llm2.invoke(prompt2)
print(result.content)
print('-' * 100)

from langchain_core.messages import SystemMessage, HumanMessage
prompt3 = [
    SystemMessage(content='당신은 창의력이 높은 작명가입니다'),
    HumanMessage(content='게임 회사를 창업하려고 하는데 이름 후보군을 3개 지어줘')
]
result = llm2.invoke(prompt3)
print(result.content)