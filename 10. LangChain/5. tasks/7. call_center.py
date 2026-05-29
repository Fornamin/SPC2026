# 질문 유형에 따라 적절한 항목으로 답변
# 질문 유형 -> 배송 조회/결제 관련/기술지원
# 러너블 브런치

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')

def make_chain(role):
    return (
        ChatPromptTemplate([
            ('system', role),
            ('user', '{question}')
        ]) | llm | StrOutputParser()
    )

payment_chain = make_chain('당신은 결제 상담원. 결제/환불/청구 문제에 대해 친절하게 답변')
delivery_chain = make_chain('당신은 배송 상담원. 배송 조회/반품/지연에 대해 친절하게 안내')
techsupport_chain = make_chain('당신은 기술 지원 담당자. 제품 설정 등 사용법과 오류를 해결하는 단계를 친절히 안내')
general_chain = make_chain('당신은 고객을 응대하는 상담원. 친절하고 간략하게 답변')

branch = RunnableBranch(
    (lambda x : any(k in x['question'] for k in ['결제', '환불', '청구']), payment_chain),
    (lambda x : any(k in x['question'] for k in ['배송', '택배', '반품']), delivery_chain),
    (lambda x : any(k in x['question'] for k in ['오류', '에러', '안돼요']), techsupport_chain),
    general_chain
)

questions = [
    '배송이 아직 안 왔어요 언제 도착해요?',
    '결제가 두 번 됐는데 한 건은 환불 부탁드립니다',
    '앱 로그인이 안 돼요 오류코드 414가 떠요',
    '이용 시간은 어떻게 되나요?'
]

for q in questions:
    print(f'Req: {q}')
    print(f'Res: {branch.invoke({'question': q})}')