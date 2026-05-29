from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.documents import Document

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')
docs = [
# --- 카테고리 1: 하드웨어 및 저장장치 (심화 및 오답 유도) ---
    Document(page_content='M.2는 SSD의 폼팩터 규격이며, SATA 방식과 NVMe 방식을 모두 지원할 수 있다.'),
    Document(page_content='PCIe 4.0 인터페이스를 사용하는 NVMe SSD는 PCIe 3.0 제품보다 이론상 2배 빠른 대역폭을 제공한다.'),
    Document(page_content='SATA3 규격의 최대 전송 속도는 초당 6Gbps(약 600MB/s) 수준에서 제한된다.'),
    Document(page_content='HDD의 성능은 디스크의 분당 회전수(RPM)에 크게 좌우되며, 주로 5400RPM과 7200RPM 제품이 쓰인다.'),
    Document(page_content='SSD는 낸드 플래시(NAND Flash) 메모리를 사용하므로 물리적인 움직임이 없어 HDD보다 충격에 강하다.'),
    Document(page_content='서버 환경에서는 데이터 안정성을 위해 NVMe 외에도 SAS(Serial Attached SCSI) 인터페이스 규격의 드라이브를 활용한다.'),
    Document(page_content='외장 SSD를 연결할 때 USB 3.2 Gen2나 썬더볼트(Thunderbolt) 규격을 사용해야 본래의 고속 성능을 낼 수 있다.'),

    # --- 카테고리 2: 프로그래밍 언어 및 기술 스택 (비교 및 확장) ---
    Document(page_content='Python은 인터프리터 언어로 개발 속도가 빠르지만, C나 C++ 같은 컴파일 언어에 비해 실행 속도는 느린 편이다.'),
    Document(page_content='JavaScript는 웹 브라우저뿐만 아니라 Node.js 런타임을 통해 서버 사이드 애플리케이션 개발에도 널리 쓰인다.'),
    Document(page_content='TypeScript는 JavaScript에 정적 타이핑을 추가하여 대규모 프로젝트에서의 에러를 방지하고 유지보수성을 높인다.'),
    Document(page_content='Rust는 가비지 컬렉터 없이도 소유권(Ownership) 시스템을 통해 메모리 안정성과 고성능을 동시에 달성한다.'),
    Document(page_content='Go(Golang)는 구글이 개발한 언어로, 고루틴(Goroutine)을 이용한 강력한 동시성 처리가 특징이다.'),
    Document(page_content='C++는 하드웨어를 직접 제어할 수 있는 강력한 성능을 제공하여 게임 엔진이나 임베디드 시스템 개발에 필수적이다.'),

    # --- 카테고리 3: 키워드는 겹치지만 맥락이 다른 문장 (검색기 교란용) ---
    Document(page_content='파이썬(Python)이라는 이름은 개발자인 귀도 반 로섬이 좋아하는 코미디 쇼 "Monty Python\'s Flying Circus"에서 유래했다.'),
    Document(page_content='자바(Java)와 자바스크립트(JavaScript)는 인도네시아의 자바 섬과 이름만 유사할 뿐, 기술적으로 완전히 다른 언어다.'),
    Document(page_content='하드디스크(HDD) 드라이브의 내부에는 데이터를 기록하는 플래터와 이를 읽는 헤드가 정밀하게 맞물려 작동한다.'),
    Document(page_content='컴퓨터의 주기억장치인 RAM은 전원이 꺼지면 데이터가 지워지는 휘발성 메모리이며, SSD나 HDD와는 역할이 다르다.'),

    # --- 카테고리 4: 아예 무관한 도메인 (임계값(Threshold) 및 필터링 테스트용) ---
    Document(page_content='에스프레소는 높은 압력으로 짧은 시간 안에 추출한 진한 이탈리아식 커피다.'),
    Document(page_content='광합성은 식물이 빛 에너지를 이용하여 이산화탄소와 물로부터 포도당을 합성하는 과정이다.'),
    Document(page_content='지구의 대기는 질소가 약 78%, 산소가 약 21%로 대부분을 차지하고 있다.')
]
embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
store = InMemoryVectorStore.from_documents(docs, embedding=embeddings)
retriever = store.as_retriever(search_kwargs={'k': 3})

prompt = ChatPromptTemplate.from_template('''
아래 문서를 참고하여 질문에 답하세요
문서\n{context}
질문\n{query}
''')

def format_docs(docs):
    # doc list -> 문자열로 반환
    return '\n\n'.join(d.page_content for d in docs)

chain = ({
    'context': retriever | format_docs, 
    'query': RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
) 
answer = chain.invoke('파이썬의 성능이나 속도 측면에서의 특징은 무엇인가요?')
print(f'Answer: {answer}')