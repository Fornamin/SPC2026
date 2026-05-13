from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 저장소 설정
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# 파일 확장자 검사
def allowed_file(file_name):
    ALLOWED_EXT = {'png', 'jpg', 'jpeg', 'gif'}

    # 파일명에 .이 여러 개 있을 수 있으므로 가장 오른쪽의 .을 기준으로 삼아야 함
    return '.' in file_name and file_name.rsplit('.')[1].lower() in ALLOWED_EXT

@app.route('/')
def index():
    html = render_template('form.html')
    return html

@app.route('/login', methods=['POST'])
def login():
    id = request.form.get('username')
    pw = request.form.get('password')           

    return render_template('login.html', name = id)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['photo']
    file_name = file.filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    
    if file and allowed_file(file_name):
        file.save(file_path)
    else:
        return f'Not supported format: {file_name}'

    return 'File Uploaded'

if __name__ == '__main__':
    app.run(debug=True)