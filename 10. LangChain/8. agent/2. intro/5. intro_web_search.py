# pip install langchain-tavily
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_tavily import TavilySearch

web_search = TavilySearch(max_results=3)
llm = ChatOpenAI(model='gpt-4o-mini')
agent = create_agent(llm, [web_search])
result = agent.invoke({
    'messages': [('user', 'LangChain의 최신 버전은?')]
})
print(result['messages'][-1].content)