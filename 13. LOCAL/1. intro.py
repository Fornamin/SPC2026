import ollama

ollama.pull('mistral')
res = ollama.chat(model='mistral', messages=[
    {'role': 'user', 'content': '인공 지능에 대해 설명해줘'}
])

print(res.message.content)