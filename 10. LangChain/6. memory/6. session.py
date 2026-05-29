from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()
llm = ChatOpenAI(model='gpt-4o-mini')

prompt = ChatPromptTemplate.from_messages([
    ('system', '당신은 친절한 한국어 어시스턴트'),
    MessagesPlaceholder('history'), 
    ('user', '{msg}')
])

chain = prompt | llm | StrOutputParser()

# 세션 관리를 위한 자료 구조
sessions = {}
sessions: dict[str, InMemoryChatMessageHistory] = {}

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in sessions:
        sessions[session_id] = InMemoryChatMessageHistory()
    return sessions[session_id]

chain_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key='msg',
    history_messages_key='history'
)

def chat(msg, session_id):
    print(f'\n[{session_id}] Question: {msg}')
    answer = chain_with_memory.invoke(
        {'msg': msg},
        config={'configurable': {'session_id': session_id}},
    )
    print(f'[{session_id}] Answer: {answer}')

user_a = 'user-A'
user_b = 'user-B'

chat('내 이름은 이몽룡입니다.', user_a)
chat('내 이름은 성춘향입니다.', user_b)
chat('저는 암행어사입니다.', user_a)
chat('저는 그네타는 것을 좋아합니다.', user_b)
chat('제가 좋아하는 음식은 비빔밥입니다.', user_a)
chat('제가 사는 곳은 남원입니다.', user_b)
chat('제가 들고 다니는 물건은 마패입니다.', user_a)
chat('제가 가장 좋아하는 계절은 봄입니다.', user_b)
chat('제가 아끼는 말의 이름은 적토마입니다.', user_a)
chat('제가 가장 좋아하는 꽃은 동백꽃입니다.', user_b)
chat('저는 누구인가요?', user_a)
chat('저는 누구인가요?', user_b)