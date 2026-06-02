from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain.agents import create_agent

import wikipedia

load_dotenv()

wikipedia.set_user_agent(
    "SPC2026Bot/1.0"
)

wiki_ko = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(
        lang='ko', top_k_results=3, doc_content_chars_max=200), 
        name='wiki_ko',
        description='Korean Wikipedia: 한국에서 일어난 사건, 개념 등'
)

wiki_en = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(
        lang='en', top_k_results=3, doc_content_chars_max=200),
        name='wiki_en',
        description='English Wikipedia: 영어권 주제 혹은 한국어 위키 정보가 부족할 때 사용'
)

llm = ChatOpenAI(model="gpt-4o-mini")

system_prompt = '''
당신은 위키피디아를 활용해 정보를 조회하고 답변하는 챗봇. 결과가 영어일 경우 한국어로 번역하여 응답.
도구 사용 가이드
- 한국 또는 한국어 관련 주제는 Korean Wikipedia에서 검색
- 글로벌/영어권 주제는 English Wikipedia에서 검색
- 검색 결과가 한 번에 나오지 않을 경우 유사어(유의어) 등으로 변경해서 재시도 가능
'''
agent = create_agent(llm, [wiki_en, wiki_ko], system_prompt=system_prompt)
question = ['파이썬은 누가 만들었어?']
result = agent.invoke({"messages": [("user", question[0])]})

print(f'{question[0]}')
for m in result['messages']:
    if hasattr(m, 'tool_calls') and m.tool_calls:
        for c in m.tool_calls:
            print(f'{c['name']} {c['args']}')
    if m.type == 'tool':
        print(f'-> {m.content[:200]}')

print(f'\n {result['messages'][-1].content}')
