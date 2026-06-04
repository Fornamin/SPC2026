# 금융 도우미 챗봇
from flask import Flask, send_from_directory
from flask import request, jsonify, session

from fin_tools import TOOLS

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage

from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

SYSTEM = '''
당신은 금융 정보 비서입니다.
- 도구를 사용해 받은 답변을 사람이 알기 쉽게 설명해주세요
- 적합한 도구가 없을 시 해당 업무를 수행할 도구가 없다는 내용만 답변하세요
'''
def ask(question: str):
    llm = ChatOpenAI(model="gpt-4o-mini")
    agent = create_agent(llm, TOOLS)
    result = agent.invoke({
        "messages": [
            SystemMessage(content=SYSTEM),
            HumanMessage(content=question),
        ]
    })

    print(f"[QUESTION] {question}")
    print(f"[RESULT] {result["messages"][-1].content}\n")
            
if __name__ == '__main__':
    print('=== Demo Command ===')
    questions = [
        '삼성전자의 주가는 현재 얼마인가요',
        '현재 한국-달러 환율은 얼마인가요',
        'NVDIA 관련 최근 뉴스는 무엇이 있나요',
        'LG생활건강은 어떤 회사인가요'
    ]
    for question in questions:
        ask(question)

    print('=== Q&A ===')
    while True:
        # 사용자로부터 질문을 받아서 exit가 올 때까지 반복
        questions = input('Enter your question: ')
        if not questions in questions.lower() in ('q', 'quit', 'exit'):
            break
        ask(questions)