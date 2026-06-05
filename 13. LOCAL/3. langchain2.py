# pip install langchain-ollama

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model='mistral')
prompt = PromptTemplate.from_template('다음 주제로 작성할만한 블로그 개요 3개를 적어줘\n주제: {topic}')
chain = prompt | llm | StrOutputParser()

print(chain.invoke({'topic': '중국어 공부'}))