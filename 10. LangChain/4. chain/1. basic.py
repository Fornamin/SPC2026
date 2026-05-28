from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()
llm = ChatOpenAI(model='gpt-4o-mini')
parser = StrOutputParser()
prompt = ChatPromptTemplate([
    ('system', '당신은 유능한 베테랑 브랜드 네이밍 전문가입니다. 반드시 1개의 제품명만 출력하세요. 설명 금지.'),
    ('user', '{company} 회사에서 {product}을(를) 만드는 제품명을 생성')
])

result = (prompt | llm | parser).invoke({'company': '유한킴벌리', 'product': '아기용 티슈'})
print(result)