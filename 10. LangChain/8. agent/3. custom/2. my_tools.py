from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

@tool
def get_word_length(word: str) -> int:
    '''단어의 글자 수를 계산해 int형으로 반환'''
    return len(word)

@tool
def calculate_tip(amount: float, percent: float) -> float:
    '''
    영수증 금액과 팁 비율을 입력받아 팁 금액을 계산한다
    
    1. 매개 변수
        - amount: 음식 가격(원/krw)
        - percent: 팁 비율(%)
    2. 예시
        10,000원에 10% 팁은 -> 1,000
    '''
    return amount * percent / 100

@tool
def search_user(user_id: str) -> dict:
    '''사용자 ID로 사용자 정보를 조회 단, 존재하지 않을 시 빈 dict를 반환({})'''
    db = {
        'user01': {'name': '홍길동', 'city': 'seoul', 'age': 20},
        'user02': {'name': '홍판서', 'city': 'seoul', 'age': 40},
        'user03': {'name': '춘삼', 'city': 'busan', 'age': 38}
    }
    return db.get(user_id, {})

tools = [get_word_length, calculate_tip, search_user]
llm = ChatOpenAI(model='gpt-4o-mini')
llm_with_tools = llm.bind_tools(tools)

print('=== Tools State ===')
for t in tools:
    print(f'[TOOL] {t.name}')
    print(f'Content: {t.description}')
    print(f'Shcema: {t.args_schema.model_json_schema()}')

print('=== Using Tools ===')
questions = [
    'this-is-a-long-sentence 문장에 글자는 몇 개?',
    '5만원 영수증에 15% 팁을 주려면?',
    '홍길동 사용자의 정보는?',
    'user02 사용자의 정보는?'
]

name2tool = {t.name: t for t in tools}

for q in questions:
    res = llm_with_tools.invoke(q)
    print(f'[QUESTION] {q}')
    for call in res.tool_calls:
        print(f' -> {call['name']} ({call['args']})')
        result = name2tool[call['name']].invoke(call['args'])
        print(f' -> [RESULT] {result}')