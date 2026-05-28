# 1. generate prompt
from langchain_core.prompts import ChatPromptTemplate 

prompt = ChatPromptTemplate.from_messages([
    ('system', '당신은 브랜드 기획자'),
    ('user', 
        '회사를 홍보하기 위한 캐치프레이즈 5개 생성'+
        '(회사명: {company}, 상품: {product})'+
        '출력 결과: ,(콤마)로 구분된 리스트(.csv)로 제공'+
        '주요 타겟: 1~20대 여성'
    )
])
filled_prompt = prompt.format(company='SONY', product='헤드셋')

# 2. call LLM
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model='gpt-4o-mini')
res = llm.invoke(filled_prompt)
print(res.content)

# 3. output-parser
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import CommaSeparatedListOutputParser

strParser = StrOutputParser()
csvParser = CommaSeparatedListOutputParser()

result_str = strParser.invoke(res)
result_csv = csvParser.invoke(res)

print(result_str, result_csv)