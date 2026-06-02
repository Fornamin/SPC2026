from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.tools import tool
from langchain.agents import create_agent

import sqlite3

load_dotenv()

conn = sqlite3.connect(':memory:', check_same_thread=False)
conn.execute(
'''
CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, city TEXT, age INTEGER);
CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price INTEGER, category TEXT);
CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, product_id INTEGER, qty INTEGER, ordered_at TEXT)

INSERT INTO users (id, name, city, age) VALUES
(1, '김민준', 'Seoul', 28),
(2, '이서연', 'Busan', 32),
(3, '박지훈', 'Incheon', 24),
(4, '최유진', 'Seoul', 29),
(5, '정다은', 'Daegu', 35);

INSERT INTO products (id, name, price, category) VALUES
(1, '노트북', 1200000, 'electronics'),
(2, '스마트폰', 900000, 'electronics'),
(3, '커피머신', 150000, 'home'),
(4, '의자', 80000, 'furniture'),
(5, '키보드', 60000, 'electronics');

INSERT INTO orders (id, user_id, product_id, qty, ordered_at) VALUES
(1, 1, 2, 1, '2026-05-01 10:15:00'),
(2, 1, 5, 2, '2026-05-03 14:20:00'),
(3, 2, 1, 1, '2026-05-10 09:00:00'),
(4, 3, 4, 1, '2026-05-12 18:45:00'),
(5, 4, 3, 1, '2026-05-15 12:30:00'),
(6, 5, 2, 1, '2026-05-18 16:10:00');
'''
)
conn.commit()

SCHEMA = '''
users(id, name, city, age)
products(id, name, price, category) -- price 단위: 원 
orders(id, user_id, product_id, ordered_at) -- user_id = users.id / product_id = products.id
'''

@tool
def run_sql(query: str) -> str:
    '''Execute query in SQLite DB and return results'''
    q = query.strip().rstrip(';')
    cur = conn.execute(q)

    cols = [d[0] for d in cur.description]
    rows = cur.fetchall()

    if not rows: return 'No Results'

    out = [' | '.join(cols)]
    out += [' | '.join(str(v) for v in row) for row in rows]
    return '\n'.join(out)

SYSTEM = f'''
당신은 SQLite 데이터 분석가이다. 아래의 스키마를 참고하여 질문에 답하라.

[스키마]
{SCHEMA}

[규칙]
 - 답변을 할 때에는 run_sql 툴을 사용하여 쿼리문을 실행
 - SQLite3 문법만을 사용 (JOIN, GROUP BY 등도 사용 가능)
'''

llm = ChatOpenAI(model='gpt-4o-mini')
agent = create_agent(llm, [run_sql], system_prompt=SYSTEM)
questions = [
    '서울 사는 사용자는 총 몇명?',
    '가장 비싼 상품 3개를 가격이 높은 순으로 보여줘',
    '김민준이 주문한 상품 이름들과 수양들을 알려줘',
    '카테고리별 총 주문 수량을 알려줘'
]

for q in questions:
    print(f'[QUESTION] {q}')
    result = agent.invoke({'message': [{'user': q}]})
    
    for m in result['messages']:
        for call in getattr(m, 'tool_calls', None) or []:
            print(f'[EXECUTED QUERY] {call['args'].get('query')}')
    print(f' -> [RESULT] {result['messages'][-1].content}\n')