# 뉴스를 입력받아서 요약/감정 분석/카테고리 분석

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')
summary_chain = (ChatPromptTemplate.from_template('다음 뉴스를 2~3문장으로 요약해줘\n{news}') 
                | llm | StrOutputParser())
sentiment_chain = (ChatPromptTemplate.from_template('다음 뉴스의 전반적 감성을 한 단어로 분석 -> 긍정/부정/중립\n{news}') 
                | llm | StrOutputParser())
category_chain = (ChatPromptTemplate.from_template('다음 뉴스의 카테고리를 한 단어로 분류 -> 사회/연예/스포츠/경제 등등\n{news}') 
                | llm | StrOutputParser())
final_chain = RunnableParallel({
    'summary': summary_chain,
    'sentiment': sentiment_chain,
    'category': category_chain
})

news = '''엘지(LG)전자 사무실에서 흉기 난동을 벌여 직원 두명을 다치게 한 협력업체 직원이 구속 갈림길에 섰다.

서울남부지법 김지현 영장전담 부장판사는 이날 오전 10시30분부터 살인미수 및 특수상해 혐의를 받는 엘지전자 협력업체 직원 정아무개(60)씨에 대한 구속 전 피의자 심문(영장실질심사)을 연다고 밝혔다. 정씨는 지난 27일 오전 서울 강서구 엘지전자 마곡업무센터에서 엘지전자 직원인 50대 남성과 40대 남성을 흉기로 찌른 혐의를 받는다.

서울 강서경찰서는 28일 정씨에 대한 구속영장을 신청하면서 “피의자는 살인의 고의가 없었다고 진술하지만, 각 피해자에 대한 범행 행위, 피해자의 피해 상황 등을 고려해 살인미수 혐의를 추가 적용했다”라며 “피해자의 상해 정도뿐 아니라 어디를 다쳤는지까지 종합적으로 보아 판단한 것”이라고 밝혔다.

경찰은 지난 27일 오전 ‘남성 두 명이 칼에 찔린 채 쓰러져 있다’는 신고를 받고 현장에 출동해 용의자를 쫓던 중 서울지하철 디지털미디어시티(DMC)역에서 ㄱ씨를 발견해 붙잡았다. 피해자들은 각각 옆구리와 팔꿈치, 팔, 어깨 등에 중상을 입고 병원으로 옮겨졌지만 생명에는 지장이 없는 상태로 알려졌다.

ㄱ씨는 경찰 조사에서 “(피해자들이) 평소 나를 하대하고 무시했다. 오늘 해고 통보를 받아 분노해 범행했다”는 취지로 진술했다고 한다. 반면 피해자 쪽은 ㄱ씨 주장을 반박하며 “평소 피의자가 업무를 버거워해 협력사 대표를 통해서만 업무 교체를 요청했다”는 취지로 진술한 것으로 전해졌다.'''

result = final_chain.invoke({'news': news})
print(f'### 뉴스 기사\n{news}\n')
print(f'### 요약\n{result['summary']}')
print(f'### 감정\n{result['sentiment']}')
print(f'### 카테고리\n{result['category']}')