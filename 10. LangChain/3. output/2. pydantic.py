from dotenv import load_dotenv

from pydantic import BaseModel, Field

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

class MovieReview(BaseModel):
    title: str = Field(description='영화 제목')
    sentiment: str = Field(description="감정 분류 (긍정, 중립, 부정)")
    score: int = Field(description='영화 별점 (1~10점)')
    summary: str = Field(description='영화 요약 (1~2줄)')
    keywords: list[str] = Field(description='핵심 키워드 (3개)')

llm = ChatOpenAI(model='gpt-4o-mini')

parser = PydanticOutputParser(pydantic_object=MovieReview)
prompt = ChatPromptTemplate.from_messages([
    '다음 영화 리뷰를 분석해주세요\n리뷰: {review}\n{format_instructions}'
    ]
)
chain = prompt | llm | parser

reviews = [
    "영화 '인터스텔라'는 우주와 시간이라는 복잡한 주제를 감동적으로 풀어낸 작품이었다. 과학적 설정도 흥미로웠고, 특히 마지막 장면에서의 감정선이 깊게 남았다.",
    "영화 '기생충'은 계급 구조를 날카롭게 풍자하면서도 스릴러적인 긴장감을 유지한 작품이다. 전개가 치밀하고 반전이 인상적이었다.",
    "영화 '어벤져스: 엔드게임'은 시리즈의 마무리답게 많은 캐릭터들의 서사를 잘 정리했고, 액션과 감동을 동시에 느낄 수 있었다.",
    "영화 '타이타닉'은 고전적인 러브스토리와 재난 영화의 요소가 잘 결합되어 있으며, 시간이 지나도 여전히 감동적인 작품이다.",
    "영화 '조커'는 한 인물의 심리 변화를 깊이 있게 보여주며 사회적 메시지를 강하게 전달하는 작품이었다. 분위기가 매우 어둡고 몰입감이 있었다.",
    "영화 '다크 나이트'는 히어로 영화의 수준을 한 단계 끌어올린 작품으로, 특히 조커 캐릭터의 존재감이 압도적이었다.",
    "영화 '라라랜드'는 음악과 색감이 아름답고 꿈과 현실 사이의 갈등을 감성적으로 잘 표현한 영화였다.",
    "영화 '인셉션'은 꿈속의 꿈이라는 독특한 설정으로 관객을 끝까지 집중하게 만드는 복잡하면서도 흥미로운 작품이다.",
    "영화 '탑건: 매버릭'은 비행 장면의 현실감과 속도감이 뛰어나고, 세대 간 이야기를 잘 엮은 속편이었다.",
    "영화 '쇼생크 탈출'은 희망과 자유라는 메시지를 조용하지만 강하게 전달하는 명작으로 평가받는다.",
    "영화 '매트릭스'는 현실과 가상세계의 경계를 다루며 철학적인 질문을 던지는 혁신적인 SF 영화였다.",
    "영화 '해리 포터와 마법사의 돌'은 마법 세계의 시작을 잘 보여주며, 어린 시절의 판타지를 충족시켜주는 작품이었다.",
    "영화 '어바웃 타임'은 시간 여행이라는 설정을 통해 사랑과 가족의 소중함을 따뜻하게 전달하는 영화였다.",
    "영화 '존 윅'은 단순한 스토리지만 액션 연출이 매우 뛰어나고 스타일리시한 장면들이 인상적이었다.",
    "영화 '미션 임파서블: 폴아웃'은 현실감 있는 액션과 긴장감 있는 전개로 끝까지 몰입하게 만드는 영화였다."
]
for review in reviews:
    result = chain.invoke({
        'review': review,
        'format_instructions': parser.get_format_instructions()
    })

    print(f'제목: {result.title}\n감정: {result.sentiment}/별점: {result.score}/요약: {result.summary}/키워드: {result.keywords}')