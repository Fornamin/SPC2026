from langchain_core.prompts import (
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate
)
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template('당신은 브랜드 기획자'),
    HumanMessagePromptTemplate.from_template(
        '회사를 홍보하기 위한 캐치프레이즈 5개 생성'+
        '(회사명: {company}, 상품: {product})'+
        '출력 결과: ,(콤마)로 구분된 리스트(.csv)로 제공 그 외 필요없음'+
        '주요 타겟: 3~50대 여성'
    )
])
inputs = {'company':'매일유업', 'product':'소화가 잘 되는 초코 우유'}

chain = prompt | ChatOpenAI(model='gpt-4o-mini') | StrOutputParser() | RunnableLambda(lambda x: {'response': x})
result = chain.invoke(inputs) # 모든 것은 체인을 호출하면서 실행된다
print(result)