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
llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.8, max_tokens=1000)

chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template('당신은 기업의 커뮤니케이션 전문가. 격식있는 어투로 이메일을 작성.'),
    HumanMessagePromptTemplate.from_template('수신자 {recipient}에게 다음 주제 {topic}에 대한 미팅 요청')
])

chain = chat_prompt | llm | StrOutputParser()

recipients = ['마케팅팀', '개발팀', '기획팀', '인사팀']
topics = ['신제품 출시 전략', '분기별 개발 성과 지표', '개인별 매출 목표치 달성 현황 리뷰', '인사 평가 리뷰']

for recipient, topic in zip(recipients, topics):
    result = chain.invoke({'recipient': recipient, 'topic': topic})  
    print(f"\n{'='*50}")
    print(f"📧 수신: {recipient} | 주제: {topic}")
    print(f"{'='*50}")
    print(result)
    print()