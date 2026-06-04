# whisper -> 음성을 기반으로 텍스트로 변환 
# STT:Speak To Text <-> TTS(Text To Speech)

import os
import base64

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def transcribe_audio(file): # 오디오를 설명
    with open(file, 'rb') as af:
        transcript = client.audio.transcriptions.create(
            model='whisper-1',
            file=af,
            response_format='text', # json 등 다양한 format
            language='ko'
        )
    return transcript

result = transcribe_audio('./file/audiosample.mp3')
print('[RESULT]', result)
print('-' * 100)
result = transcribe_audio('./file/audiosample2.mp3')
print('[RESULT]', result)