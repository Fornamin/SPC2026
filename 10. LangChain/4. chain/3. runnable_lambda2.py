from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser
from langchain_core.runnables import RunnableLambda

load_dotenv()

prompt = ChatPromptTemplate.from_template(
    '{product}을/를 만드는 회사의 이름을 하나 추천 +답변은 이름만 출력'
)
llm = ChatOpenAI(model='gpt-4o-mini')
chain = prompt | llm | StrOutputParser()
result = chain.invoke({'product': '의류'}) 
print(format(result))
print('-' * 100)

prompt = ChatPromptTemplate.from_template(
    '{topic}과/와 관련된 키워드 5개를 쉼표(,)로 구분해서 나열'
)
chain = prompt | llm | CommaSeparatedListOutputParser()
result = chain.invoke({'topic': '인공 지능'}) # list
print(result)
print('-' * 100)

prompt_name = ChatPromptTemplate.from_template(
    '{product}을/를 만드는 회사의 이름을 하나 추천 +답변은 이름만 출력'
)
prompt_slogan = ChatPromptTemplate.from_template(
    '{company} 회사의 캐치 프레이즈를 작성 + 답변은 캐치 프레이즈만 출력'
)

chain = (prompt_name 
        | llm 
        | StrOutputParser() 
        | RunnableLambda(lambda name: {'company': name.strip()})
        | prompt_slogan
        | llm
        | RunnableLambda(lambda slogan: {'slogan': slogan})
)
result = chain.invoke({'product': '악세사리'})
print(result)