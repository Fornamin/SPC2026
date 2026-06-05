from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()
model = 'claude-opus-4-8'
prompt = '''
함수 f(x)=x^2−4x−3에 대하여, 곡선 y=f(x) 위의 점 (1,−6)에서의 접선을 l이라 하고,
함수 g(x)=(x^3−2x)f(x)
에 대하여, 곡선 y=g(x) 위의 점 (1,6)에서의 접선을 m이라 한다.
두 직선 l,m과 y-축으로 둘러싸인 도형의 넓이를 구하여라.

풀이는 마크다운을 사용하지 않고 한국어로만 대답
'''

with client.messages.stream(
    model=model,
    max_tokens=2500,
    thinking={'type': 'adaptive', 'display': 'summarized'},
    messages=[{'role': 'user', 'content': prompt}]
) as stream:
    for event in stream:
        if event.type == 'content_block_start':
            if event.content_block.type == 'thinking':
                print(f'\n[Thinking] ', end='', flush=True)
            elif event.content_block.type == 'text':
                print('\n\n[Response] ', end='', flush=True)
        elif event.type == 'content_block_delta':
            if event.delta.type == 'thinking_delta':
                print(event.delta.thinking, end='', flush=True)
            elif event.delta.type == 'text_delta':
                print(event.delta.text, end='', flush=True)
print()