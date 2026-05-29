from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
llm = ChatOpenAI(model='gpt-4o-mini')

prompt = ChatPromptTemplate.from_messages([
    ('system', '당신은 친절한 챗봇'),
    MessagesPlaceholder('history'), # history라고 key를 지정
    ('user', '{msg}')
])

chain = prompt | llm | StrOutputParser()
history_example = [
    HumanMessage(content='안녕. 나는 홍길동.'),
    AIMessage(content='네, 홍길동님 반갑습니다.')
]
answer = chain.invoke({
    'history': history_example,
    'msg': '내 이름이 뭐게?'
})

print(answer)