from dotenv import load_dotenv
from anthropic import Anthropic
import time

load_dotenv()

client = Anthropic()
models = ['claude-haiku-4-5', 'claude-sonnet-4-6', 'claude-opus-4-7', 'claude-opus-4-8']
prompt = '인공지능과 LLM의 동작 원리를 컴퓨터학 전공자가 이해할 수 있는 정도로 설명해줘'

for model in models:
    start = time.time()
    msg = client.messages.create(
        model=model,
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )
    elasped = time.time() - start
    text = msg.content[0].text

    print(f'[{model}] {elasped:.1f} Sec / {msg.usage.output_tokens} Tokens')
    print(f'[RESPONSE] {text}')