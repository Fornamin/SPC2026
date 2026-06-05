from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()
messages = []

def chat(message: str) -> str:
    print(f'[QUESTION] {message}')
    messages.append({'role': 'user', 'content': message})

    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=300,
        temperature=1.0,
        messages=messages
    )
    messages.append({'role': 'assistant', 'content': response.content[0].text})
    return response.content[0].text

print(f'[ANSWER] {chat("안녕 나는 김철수야")}')
print(f'[ANSWER] {chat("그래서 내가 누구라고?")}')