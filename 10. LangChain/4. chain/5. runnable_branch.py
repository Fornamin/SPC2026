from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda

load_dotenv()
llm = ChatOpenAI(model='gpt-4o-mini')

def make_chain(role):
    prompt = ChatPromptTemplate.from_messages([
        ('system', role),
        ('user', '{question}')
    ])

    return prompt | llm | StrOutputParser()

code_chain = (
    make_chain('당신은 파이썬 개발자')
    | RunnableLambda(lambda x: print("=== code_chain ===") or x)
)
cook_chain = (
    make_chain('당신은 요리 전문가')
    | RunnableLambda(lambda x: print("=== cook_chain ===") or x)
)
general_chain = (
    make_chain('당신은 일반 어시스턴트')
    | RunnableLambda(lambda x: print("=== general_chain ===") or x)
)

branch = RunnableBranch(
    (
        lambda x: '파이썬' in x['question'] or '코드' in x['question'],
        code_chain
    ),
    (
        lambda x: '요리' in x['question'] or '레시피' in x['question'],
        cook_chain
    ), general_chain
)

questions = [
    '파이썬 리스트 정렬 코드 예제를 작성',
    '김치찌개 레시피',
    '요즘 날씨 어때?',
]

for q in questions:
    print('질문: ', q)
    print('답변: ', branch.invoke({'question': q}))