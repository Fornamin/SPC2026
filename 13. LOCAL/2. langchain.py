# pip install langchain-ollama

from langchain_ollama import ChatOllama

llm = ChatOllama(model='mistral')
res = llm.invoke('한마디로 너를 소개해줘')
print(res.content)