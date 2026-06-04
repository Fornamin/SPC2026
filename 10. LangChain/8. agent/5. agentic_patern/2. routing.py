from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()
llm = ChatOpenAI(model='gpt-4o-mini')
parser = StrOutputParser()

technical_prompt = ChatPromptTemplate.from_template(
    '당신은 기술 지원 전문가\n'
    '정확하고 단계 별로 문제를 해결하는 방법을 안내\n'
    '고객 문의: {question}'
)
technical_chain = technical_prompt | llm | parser

billing_prompt = ChatPromptTemplate.from_template(
    '당신은 결제 및 구독 전문 상담원\n'
    '사내 정책에 따라 친절하게 안내 및 응대\n'
    '- 사내 정책'
    '\t1. 환불 또는 회원 탈퇴를 원할 경우 불만족에 대한 사과 후 다른 상품을 권유 및 가입을 유도'
    '\t2. 환불은 미개봉 상품일 경우 일주일 이내로 가능'
    '고객 문의: {question}'
)
billing_chain = billing_prompt | llm | parser

general_prompt = ChatPromptTemplate.from_template(
    '당신은 고객 서비스 담당\n'
    '고객의 질문에 대해 친절하게 답변\n'
    '고객 문의: {question}'
)
general_chain = general_prompt | llm | parser

route_map = {
    'technical': technical_chain,
    'billing': billing_chain,
    'general': general_chain
}

# Routing
def route_query(input: dict) -> str:
    question = input['question']

    # 1. Classfication
    classifier_prompt = ChatPromptTemplate.from_template(
        '고객의 문의를 보고 어느 카테고리에 해당하는 지 분류\n'
        '반드시 아래 카테고리 중 하나로만 출력\n'
        'technical / billing / general'
        '고객 문의: {question}'
    )
    classifier_chain = classifier_prompt | llm | parser
    category = classifier_chain.invoke({'question': question}).strip().lower()
    print(f'[CATEGORY] {category}')

    # 2. 
    chain = route_map.get(category, general_chain)
    res = chain.invoke({'question': question})

    return f'[{category.upper()}] {res}'

routing_chain = RunnableLambda(route_query)

# Result
test_questions = [
    '프로그램이 자꾸 충돌하는데 어떻게 해야해요?',
    '구독을 취소하고 환불받고 싶어요',
    '이 서비스는 어떤 기능을 제공하나요?',
    'API 연동 시 인증 오류가 발생해요'
]

for i, question in enumerate(test_questions, 1):
    print(f'[QUESTION{i}] {question}')
    result = routing_chain.invoke({'question': question})
    print(f'[ANSWER] {result}')