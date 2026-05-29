from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

# 기타(히스토리)
from langchain_community.chat_message_histories import SQLChatMessageHistory
from sqlalchemy import create_engine

load_dotenv()

DB_URL = 'sqlite:///chat_history.db'
SESSION_ID = 'default'

engine = create_engine(DB_URL)
history = SQLChatMessageHistory(session_id=SESSION_ID, connection=engine)

llm = ChatOpenAI(model='gpt-4o-mini')

prompt = ChatPromptTemplate.from_messages([
    ('system', '당신은 친절한 챗봇'),
    MessagesPlaceholder('history'), 
    ('user', '{msg}')
])

chain = prompt | llm | StrOutputParser()

def chat(msg):
    print('Question:', msg)
    answer = chain.invoke({
        'history': history.messages[-10:],
        'msg': msg
    })
    print('Answer:', answer)

    history.add_user_message(msg)
    history.add_ai_message(answer)

chat('저는 어떤 사람인가요')