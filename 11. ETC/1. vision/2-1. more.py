import base64
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)
image_path = "./file/maxresdefault.jpg" 

# 1. 로컬 이미지를 base64 문자열로 변환하는 함수
def encode_img(path):
    with open(path, "rb") as f: 
        return base64.b64encode(f.read()).decode("utf-8")


# 2. 질문과 base64 이미지를 받아 OpenAI API를 호출하는 함수
def ask_about_image(question, b64):  # question 매개변수를 추가했습니다.
    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": question,},  
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"},},
            ]}
        ]
    )
    return res.choices[0].message.content

# 3. 이미지 인코딩 및 반복문을 통한 질문 수행
b64 = encode_img(image_path)
questions = [
    "이미지에 있는 한글 글자를 다 읽어줘",
    "해당 이미지에 사용된 주요 색상을 알려줘",
    "이미지의 전체 분위기를 한 문장으로 표현하면?",
]

for question in questions:
    print(f"[QUESTION] {question}")
    print(f"[ANSWER] {ask_about_image(question, b64)}")
    print("-" * 50)  
