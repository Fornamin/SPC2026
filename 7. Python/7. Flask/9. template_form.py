from flask import Flask, render_template, request
import os

app = Flask(__name__)

# 저장소 설정
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


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
    file.save(file_path)

    return 'File Uploaded'

if __name__ == '__main__':
    app.run(debug=True)