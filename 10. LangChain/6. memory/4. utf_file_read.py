import json
import sys
from pprint import pprint

with open('history.json', 'r', encoding='utf-8') as f:
    messages = json.load(f)
pprint(messages)
ROLE = {'human': '사용자', 'ai': '챗봇', 'system': '시스템'}

print(f'=== {len(messages)} ===')
for i, m in enumerate(messages, 1):
    role = ROLE.get(m.get('type'), m.get('type)'))
    msg = m.get('data').get('content')
    print(f'{i:02d}. [{role}]: {msg}')