from dotenv import load_dotenv
# 모델
from langchain_openai import ChatOpenAI
# 프롬프트
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# 파서
from langchain_core.output_parsers import StrOutputParser
# 기타(히스토리)
from langchain_core.chat_history import InMemoryChatMessageHistory

load_dotenv()
llm = ChatOpenAI(model='gpt-4o-mini')

prompt = ChatPromptTemplate.from_messages([
    ('system', '당신은 친절한 챗봇'),
    MessagesPlaceholder('history'), 
    ('user', '{msg}')
])

chain = prompt | llm | StrOutputParser()
history = InMemoryChatMessageHistory()

def chat(msg):
    print('Question:', msg)
    answer = chain.invoke({
        'history': history.messages[-10:],
        'msg': msg
    })
    print('Answer:', answer)

    history.add_user_message(msg)
    history.add_ai_message(answer)

chat('안녕하세요 제 이름은 곽형수입니다')
chat('저는 겨울에 바다에 가서 서핑하는 것을 좋아합니다')
chat('저는 어떤 사람인가요')