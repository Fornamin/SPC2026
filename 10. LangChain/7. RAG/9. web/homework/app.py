from flask import Flask, request, jsonify, render_template
import os
# 1. 랭체인 기본 불러오기
# 2. 문서 파서 기본 불러오기
# 3-1. 벡터 스토어 셋업
# 3-2. 랭체인 셋업 (LCEL)

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.get('/')
def index():
    return render_template('index.html')

@app.post('/upload')
def upload():
    files = request.files['file-input']
    

    return jsonify({'msg': 200})

@app.post('/ask')
def ask():
    return jsonify({'msg': 200})

if __name__ == '__main__':
    app.run(debug=True)