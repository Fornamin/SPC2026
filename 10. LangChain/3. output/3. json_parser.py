from dotenv import load_dotenv

from pydantic import BaseModel, Field

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')
parser = JsonOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ('system', '답변은 무조건 json / 설명 X'),
    ('user', '{question}\n\n{format_instructor}')
]).partial(format_instructor=parser.get_format_instructions())
result = (prompt | llm | parser).invoke({
    'question': '아시아에서 인구가 가장 많은 나라 3개의 국가명과 수도를 알려줘'
    })
print(result)