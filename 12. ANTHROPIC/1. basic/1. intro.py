from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

response = client.messages.create(
    # haiku(빠름), sonnet, opus(최신)
    model="claude-sonnet-4-0",
    max_tokens=300,
    messages=[
        {
            "role": "user",
            "content": "안녕하세요. 자기소개를 해주세요."
        }
    ]
)

print(response.content[0].text)