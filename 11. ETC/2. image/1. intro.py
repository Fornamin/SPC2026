# 텍스트를 기반으로 이미지 생성 -> GAN
# dall-e -> ... -> gpt-image-2(NOW)
import os
import base64

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
prompt = '에곤 쉴레 스타일, 침대에 누워있는 인간, 연필 드로잉'
result = client.images.generate(
    model = 'gpt-image-1.5',
    prompt = prompt,
    size = '1024x1024',
    quality = 'high' # low / medium / high
)

b64 = result.data[0].b64_json
with open('output3.png', 'wb') as f:
    f.write(base64.b64decode(b64))
print('=== SAVE ===')