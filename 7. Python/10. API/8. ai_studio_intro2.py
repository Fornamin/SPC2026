# New Version
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
res = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='안녕하세요'
)
print(res.text)

# chat = client.chats.create(model="gemini-2.5-flash")
# result = []
# result.append(chat.send_message("대화기록 ㄱㄱ").text)
# result.append(chat.send_message("ㅎㅇ").text)

# print(result)