import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, Response
import json

import openai

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=openai_api_key)

app = Flask(__name__)
chat_history = []

curriculums = {
    1: ['기초 인사', '간단한 문장', '동물 이름'],
    2: ['학교 생활', '가족 소개', '자기 소개'],    
    3: ['취미와 운동', '날씨 묘사', '간단한 이야기'],
    4: ['쇼핑과 가격', '음식 주문', '여행 이야기'],
    5: ['역사와 문화', '과학과 자연', '사회 이슈'],
    6: ['미래 계획', '진로 탐색', '세계 여행']
}

@app.route('/')
def home():
    return render_template('home.html', grades = curriculums.keys())

@app.route('/grade/<int:grade>')
def grade(grade):
    if grade in curriculums:
        curriculums_index = list(enumerate(curriculums[grade]))
        return render_template('grade.html', grade=grade, grades=curriculums.keys(), curriculums=curriculums_index)
    return '존재하지 않는 학년입니다', 404

@app.route('/grade/<int:grade>/curriculum/<int:curriculum_id>')
def curriculum(grade, curriculum_id):
    if grade in curriculums and 0 <= curriculum_id < len(curriculums[grade]):
        curriculum_title = curriculums[grade][curriculum_id]
        return render_template('curriculum.html', grade=grade, grades=curriculums.keys(), curriculum_title=curriculum_title)
    return '해당 커리큘럼은 존재하지 않습니다', 404

@app.route('/chat', methods=['POST'])
def chat(): 
    message = request.json.get('message', '')
    baseURI = request.json.get('baseURI', '')
    parsedURI = baseURI.split('/')  
    
    grade = parsedURI[4]
    curriculum_title = curriculums[int(grade)][int(parsedURI[6])]
        
    prompt = f'''
    당신은 친절한 영어 선생님입니다.
    학생은 대한민국 초등학교 {grade}학년 학생입니다.
    대화의 주제는 {curriculum_title}이며 주제에 벗어나면 주제로 돌아오도록 대화를 이끌어주세요.
    학생이 이해하기 어려운 단어나 표현이 나오면 친절하게 설명해주세요.
    한국어를 사용하지 말고 영어로만 대답해주세요.'''

    chat_history.append({
            "role": "user",
            "content": message
    })

    def generate_response():
        reply = ''
        res = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[{'role': 'system', 'content': prompt}] + chat_history[-10:],
            stream=True
        )
        for chunk in res:
            content = chunk.choices[0].delta.content
            if content:
                reply += content
                yield f'data: {json.dumps({'content': content}, ensure_ascii=False)}\n\n'
        
        chat_history.append({
            "role": "system",
            "content": reply
        })

        yield 'data: [DONE]\n\n'

    return Response(generate_response(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True)