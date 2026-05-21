import imaplib
import email
from email.header import decode_header

import os
from dotenv import load_dotenv

load_dotenv()

IMAP_SERVER = 'imap.naver.com'
IMAP_PORT = 993

NAVER_ID = os.getenv('NAVER_ID')
NAVER_PASSWORD = os.getenv('NAVER_MAIL_APP_SECRET')
NAVER_EMAIL = f'{NAVER_ID}@naver.com'

mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
mail.login(NAVER_EMAIL, NAVER_PASSWORD)

mail.select('INBOX')
status, messages = mail.search(None, 'ALL')

mail_ids = messages[0].split()
lastest_mail_id = mail_ids[-1]

# print('My Mails: ', mail_ids)
# print('The Lastest Mail: ', lastest_mail_id)

status, msg_data = mail.fetch(lastest_mail_id, '(RFC822)')
# print(status)
# print(msg_data)

# Mail Data Body Parsing
for res_part in msg_data:
    if isinstance(res_part, tuple):
        # Mail Data Decoding
        msg = email.message_from_bytes(res_part[1])

        # Mail Title Decoding
        subject, encoding = decode_header(msg['Subject'])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else 'utf-8')

        print('Title: ', subject)

        from_ = msg.get('From')
        print('From: ', from_)

        # Mail Body
        if msg.is_multipart():
            print('지금은 생략')
        else:
            body = msg.get_payload(decode=True).decode('utf-8')
            print('Body: ', body)