import smtplib
from email.mime.text import MIMEText

import os
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = 'smtp.naver.com'
SMTP_PORT = 587

NAVER_ID = os.getenv('NAVER_ID')
NAVER_PASSWORD = os.getenv('NAVER_MAIL_APP_SECRET')
NAVER_EMAIL = f'{NAVER_ID}@naver.com'

subject = '[TEST] Sending a mail'
body = """
<html>
    <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 30px;">
        <div style="
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        ">
            <h1 style="color: #03C75A; text-align: center;">
                📧 Python Mail Test
            </h1>

            <p style="font-size: 16px; color: #333;">
                Hello 👋
            </p>

            <p style="font-size: 15px; line-height: 1.6; color: #555;">
                This mail is made by <b>Python</b>.
                <br><br>
                HTML styling is successfully applied ✨
            </p>

            <div style="text-align: center; margin-top: 30px;">
                <a href="https://www.python.org"
                   style="
                        background-color: #3776AB;
                        color: white;
                        padding: 12px 20px;
                        text-decoration: none;
                        border-radius: 8px;
                        display: inline-block;
                   ">
                    Visit Python
                </a>
            </div>

            <hr style="margin-top: 40px;">

            <p style="font-size: 12px; color: gray; text-align: center;">
                Sent automatically using Python SMTP
            </p>
        </div>
    </body>
</html>
"""

# MIMETYPE: 이메일 작성 타입(인코딩)
# message = MIMEText(body, _charset='utf-8')
message = MIMEText(body, 'html', _charset='utf-8') # HTML일 경우 formatting 필요
message['Subject'] = subject
message['From'] = NAVER_EMAIL
message['To'] = NAVER_EMAIL
message['Body'] = body

try:
    smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp.starttls() # TLS 보안 연결
    smtp.login(NAVER_ID, NAVER_PASSWORD)
    smtp.sendmail(NAVER_EMAIL, message['To'], message.as_string())
    print('Sending a mail successed')
except Exception as e:
    print(f'Error: {e}')
finally:
    smtp.quit()