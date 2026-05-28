# 목적: 필요한 비즈니스 로직에 맞는 SQL 구문을 작성
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate, 
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate
)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda

load_dotenv()

schema = '''-- 사용자
CREATE TABLE users (
    id          INT PRIMARY KEY AUTO_INCREMENT,
    username    VARCHAR(50)  NOT NULL UNIQUE,
    email       VARCHAR(100) NOT NULL UNIQUE,
    password    VARCHAR(255) NOT NULL,
    created_at  DATETIME     DEFAULT CURRENT_TIMESTAMP
);

-- 상품
CREATE TABLE products (
    id          INT PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(100) NOT NULL,
    price       INT          NOT NULL,
    stock       INT          DEFAULT 0,
    created_at  DATETIME     DEFAULT CURRENT_TIMESTAMP
);

-- 주문 (users, products 연결)
CREATE TABLE orders (
    id          INT PRIMARY KEY AUTO_INCREMENT,
    user_id     INT          NOT NULL,
    product_id  INT          NOT NULL,
    quantity    INT          DEFAULT 1,
    status      VARCHAR(20)  DEFAULT 'pending',  -- pending / paid / shipped / done
    ordered_at  DATETIME     DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)    REFERENCES users(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);'''
requests = [
    '주문 상태가 "paid"인 주문 중, 총 결제금액이 가장 높은 유저의 이름과 총 결제금액을 조회하시오',
    '상품별 총 주문 수량을 구하되, 총 주문 수량이 10개 이상인 상품만 이름과 함께 조회하시오.',
    '한 번도 주문한 적 없는 유저의 이름과 이메일을 조회하시오.'
]

chat_prompt = ChatPromptTemplate.from_messages([
    ('system', '당신은 DB 전문가. 답변에는 SQL 쿼리만 존재해야함.'),
    ('human', '[DB schema]\n{schema}\n[User Request]{request}')
])
llm = ChatOpenAI(model='gpt-4o-mini', temperature=0, max_tokens=1000)
chain = chat_prompt | llm | RunnableLambda(lambda x: {'sql': x.content.strip()})

for idx, request in enumerate(requests, start=1):
    print(f'Req #{idx}] {request}')
    result = chain.invoke({'schema': schema, 'request': request})
    print(f'Res]\n{result["sql"]}')