from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.tools import tool

from pprint import pprint
import json
from typing import Literal
from pydantic import BaseModel, Field

class SendEmailInput(BaseModel):
    '''Email Sending Tool's Arguments'''
    to: str = Field(description='수신자 이메일 주소(반드시 유효한 이메일 형식)')
    subject: str = Field(description='이메일 제목(50자 이내)')
    body: str = Field(description='이메일 본문')
    priority: Literal['low', 'normal', 'high'] = Field(
        default='normal', description='우선순위 / 긴급한 경우에는 high 사용')

@tool(args_schema=SendEmailInput)
def send_email(to: str, subject: str, body: str, priority: str='normal') -> str:
    '''사용자가 요청할 때 이메일을 전송하기 위한 도구.'''
    print(f'[Mail Send] To: {to}, Priority: {priority}')
    print(f'[Subject] {subject}')
    print(f'[Body] {body}')
    return f"메일 전송 완료 → to={to}, subject={subject}, priority={priority}"

class SearchInput(BaseModel):
    '''Searching Tool's Arguments'''
    query: str = Field(description='검색어')
    max_results: int = Field(description='')
    sort_by: Literal['relevance', 'date'] = Field(
        default='relevance',
        description='정렬 기준 (최신순을 원할 시 date를 사용)'
    )

@tool(args_schema=SearchInput)
def search(query: str, max_results: int=5, sort_by: str='relevance') -> list[str]:
    '''Execute searcing by query'''
    return [f'[Result]\n{i}. {query} (Sorting by {sort_by})' for i in range(max_results)]

llm = ChatOpenAI(model='gpt-4o-mini')
llm_with_tools = llm.bind_tools([send_email, search])

print('=== Tools State ===')
pprint(json.dumps({
    "send_email": send_email.args_schema.model_json_schema(),
    "search": search.args_schema.model_json_schema(),}, 
    indent=2, 
    ensure_ascii=False))

print('\n=== Using Tools ===')
questions = [
    'alice@example.com에게 회의 일정 변경 메일 전송. 회의가 내일 오후 3시로 변경됨. 긴급.',
    '파이썬 비동기 프로그래밍 최신 자료 5개만 날짜순으로 검색해줘',
    '내일 샌드위치를 만들건데 레시피를 알려줘'
]

SYSTEM = (
    '도구는 적합할 때만 사용. '
    '입력 인자를 잘 확인하고 오류가 없도록 호출. '
    '호출 이후 오류가 발생한 경우 도구의 목적과 인자값을 잘 확인하고 최대 2회 재시도. '
    '적합한 도구가 없을 경우 해당 작업을 수행할 수 있는 도구가 없다는 내용만 답변해야함'
)
name2tool = {t.name: t for t in [send_email, search]}
for q in questions:
    print(f'[QUESTION] {q}')
    res = llm_with_tools.invoke([SystemMessage(SYSTEM), HumanMessage(q)])
    
    if not res.tool_calls:
        print(f'[NOT USING TOOL] {res.content}')
    else:
        for call in res.tool_calls:
            # print(f' -> {call['name']} ({call['args']})')
            result = name2tool[call['name']].invoke(call['args'])
            print(f' -> [RESULT] {result}\n')