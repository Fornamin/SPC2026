from flask import Flask, request, jsonify

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')
app = Flask(__name__)

@app.route('/api/name')
def recommend_name_company():
    prompt = [
        SystemMessage(content='당신은 창의적인 브랜딩 전문가입니다.'),
        HumanMessage(content='PC 게임을 개발하는 회사명을 지어줘.')
    ]
    result = llm.invoke(prompt)
    print(result.content)

    return jsonify({'result': 'success', 'chatbot': result.content})

@app.route('/api/name', methods=['POST'])
def recommend_name_product():
    data = request.get_json()
    product = data.get('product')

    prompt = [
        SystemMessage(content='당신은 창의적인 브랜딩 전문가입니다.'),
        HumanMessage(content=f'{product}을 개발하는 회사명을 지어줘.')
    ]
    result = llm.invoke(prompt)
    print(result.content)

    return jsonify({'result': 'success', 'chatbot': result.content})

@app.route('/api/dinner')
def recommend_dinner():
    prompt = [
        SystemMessage(content='당신은 경력 10년차 호텔 쉐프입니다.'),
        HumanMessage(content='오늘 저녁 메뉴를 추천해줘.')
    ]
    result = llm.invoke(prompt)
    print(result.content)

    return jsonify({'result': 'success', 'chatbot': result.content})

if __name__ == '__main__':
    app.run(debug=True)