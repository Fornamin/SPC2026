# pip install lxml
from dotenv import load_dotenv

import base64, requests
from bs4 import BeautifulSoup

from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

load_dotenv()
llm = ChatOpenAI(model='gpt-4o-mini')
client = OpenAI()

def fetch_news(query):
    '''뉴스 검색 결과를 가져온다'''
    url = 'https://news.google.com/rss/search'
    params = {
        'q': query,
        'hl': 'ko',
        'gl': 'KR',
        'ceid': 'KR:ko'
    }
    xml = requests.get(url, params=params, timeout=10).text
    soup = BeautifulSoup(xml, 'xml')
    items = []
    
    for item in soup.find_all('item')[:8]:
        print(item)
        items.append({
            'title': item.title.text,
            'date': item.pubDate.text,
            'link': item.link.text
        })

def make_img_prompt(news):
    prompt = f'''
        다음 뉴스 내용을 바탕으로 웹툰형 카드뉴스 이미지 생성 프롬프트를 만드세요

        조건:
         - 한 장의 이미지
         - 여러 컷으로 이루어진 웹툰 스타일
         - 한국어 텍스트 포함
         - 뉴스 카드 + 만화 컷 + 인포그래픽 형태로 혼합하여 구성
         - 실제 해당 유명인을 캐릭터화해서 등장인물로 생성
         - 회사 로고나 상표 등을 적절하게 활용해서 실제 내용을 실감나게 살림

        뉴스:
        {news}
    '''
    result = llm.invoke(prompt)
    return result.content

def generate_img(img_prompt, output='news.png'):
    result = client.images.generate(
        model='gpt-image-1.5',
        prompt=img_prompt,
        size='1024x1024',
        quality='medium'
    )

    img_base64 = result.data[0].b64_json
    with open(output, 'wb') as f:
        f.write(base64.b64decode(img_base64))

    return output

news_agent = create_agent(
    model=llm,
    tools=[fetch_news],
    system_prompt='''
        당신은 뉴스 조사 에이전트. 사용자 주제와 관련된 뉴스 목록을 수집하고 일정/날짜/행사/만남 정보를 중심으로 정리
    '''
)

def main():
    story = '젠슨 황 4박 5일 한국 방문 일정'
    # 1. 뉴스 수집
    news_result = news_agent.invoke({
        'messages': [
            {'role': 'user', 'content': story}
        ]
    })

    news = news_result['messages'][-1].content
    print(news)

    # # 2. 뉴스 요약 및 이미지 생성
    # img_prompt = make_img_prompt(news)
    # print(img_prompt)

    # # 3. 이미지 생성
    # output_file = generate_img(img_prompt)
    # print(f'\n이미지 생성 완료: {output_file}')

main()