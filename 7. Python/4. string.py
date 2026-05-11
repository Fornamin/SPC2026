# 문자열을 할당하면 stirng 타입이 됨
s = 'Hello, World'

print(s)
print(s.lower())
print(s.upper())
print(s.capitalize()) # 각 문장의 시작은 대문자
print(s.title()) # 각 단어의 시작은 소문자

s = '       Hello,          World    '
print(s.strip()) # 앞 뒤 불필요한 공백 제거
print(s.lstrip())
print(s.rstrip())
print(s.split())

s = 'apple banana cherry'
print(s.split())
s = 'apple,banana,cherry' # csv -> comma seperated value
print(s.split(','))

s_list = s.split(',') # list를 담고 있는 자료 구조
print(','.join(s_list)) # list를 comma로 합쳐라

s = 'Hello, World'
print(s.startswith('Hello'))
print(s.startswith('hello'))
print(s.endswith('World'))
print(s.find('World')) # output: 7 -> idx: 7에 위치
print(s.find('world')) # output: -1 -> not found

s = '홍길동'
print(s.startswith('홍'))
print(s.endswith('동'))