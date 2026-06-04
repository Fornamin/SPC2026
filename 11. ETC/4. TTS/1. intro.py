import os
import base64

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

text = '안녕하세요. OpenAI의 음성 생성 예제입니다. 학습자 분은 김민정님입니다.'
res = client.audio.speech.create(
    model='tts-1',
    voice='alloy',
    input=text
)

res.write_to_file('./file/audio/output.mp3')
print('[SAVE]')