from flask import Flask, send_from_directory
from flask import request, jsonify, session

import os
from dotenv import load_dotenv

import openai

app = Flask(__name__, static_folder="public")
app.secret_key = 'your_secret_key'

openai_api_key = os.getenv("OPENAI_API_KEY")
openai_client = openai.OpenAI(api_key=openai_api_key)

reviews = []  # 사용자들의 댓글을 저장할 변수 (평점과 후기가 함께 들어간다. {'rating': 값, 'comment': 값})
language = {
    'kr': '한국어',
    'en': '영어',
    'jp': '일본어'
}

# ------------------
# API 라우팅
# ------------------
@app.route('/api/translate', methods=['POST'])  # POST로 받기
def translate_review():
    message = request.json.get('message')

    def ask_chatgpt():
        res = openai_client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[{'role': 'system', 'content': f'이 댓글을 {session['current_language']}로 번역해줘.'},
                      {'role': 'user', 'content': message }]
        )
        return res.choices[0].message.content

    return jsonify({'translated_message': ask_chatgpt()})

@app.route('/api/reviews', methods=['POST'])  # POST로 받기
def add_review():
    reviews.append({'rating': request.json.get('rating'), 'comment': request.json.get('comment')})

    return jsonify({'rating': request.json.get('rating'), 'comment': request.json.get('comment')})

@app.route('/api/reviews')  # GET으로 받기
def get_review():
    return jsonify(reviews)

@app.route('/api/ai-summary')   # GET으로 받기
def get_ai_summary():
    # reviews를 가져와서....
    # 여기에서 프롬프트 및 api 호출 코드 작성
    ratings = 0
    total_comment = []
    for item in reviews:
        ratings += int(item['rating'])
        total_comment.append(item['comment'])

    if len(reviews) == 0:
        return jsonify({'message': '아직 리뷰가 없습니다', 'total_rating': 'N/A'})
    total_rating = ratings / len(reviews)

    def ask_chatgpt():
        res = openai_client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[{'role': 'system', 'content': f'이 쇼핑몰 상품의 리뷰들과 평균 별점의 읽고 전반적인 경향을 2줄 이내로 간단하게 요약해줘 언어는 {session['current_language']}로 작성해줘.'},
                      {'role': 'user', 'content': f'평균 별점: {total_rating}, 리뷰란: {total_comment}'}]
        )
        return res.choices[0].message.content
    return jsonify({'message': ask_chatgpt(), 'total_rating': total_rating})

# ------------------
# 웹 서비스 라우팅
# ------------------
@app.route('/')
def index():
    session['current_language'] = language['kr']

    return send_from_directory('public', 'index.html')

@app.route('/<lang>')
def index_lang(lang):
    for key, value in language.items():
        if key == lang:
            session['current_language'] = value

    return send_from_directory('public', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)