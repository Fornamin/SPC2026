from dotenv import load_dotenv

from pydantic import BaseModel, Field

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()
llm = ChatOpenAI(model='gpt-4o-mini')
parser = StrOutputParser()
prompt = ChatPromptTemplate([
    ('system', '당신은 유능한 베테랑 기획자'),
    ('user', '{company} 회사에서 {product}을(를) 만드는데 이 제품명을 생성')
])

chain = prompt | llm | parser | RunnableLambda(lambda x: {"response": x})

result = chain.invoke({
    'company': '유한킴벌리',
    'product': '아기용 티슈'
})

print(result["response"])