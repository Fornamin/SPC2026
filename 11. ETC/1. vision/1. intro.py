# 1. 사진을 직접 올린다 (base64 인코딩)
# 2. 이미지 URL을 주고 읽기
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

image_url = 'https://i.ytimg.com/vi/1TovhBXTAQE/maxresdefault.jpg'
res = client.chat.completions.create(
    model='gpt-4o-mini',
    messages = [
        {
            'role': 'user',
            'content': [
                {'type': 'text', 'text': '이 이미지를 한국어로 설명해줘'},
                {'type': 'image_url', 'image_url': {'url': image_url}}
            ]
        }
    ]
)
print(res.choices[0].message.content)