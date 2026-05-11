print('-' * 100)
for i in range(1, 6): # 1부터 6 미만까지 (1 ~ 5)
    print('*' * i)

print('-' * 100)
for i in range(1, 6):
    print((' ' * (5 - i)), end = '') # 공백을 출력하는 부분
    print('*' * i) # 별을 출력하는 부분

print('-' * 100)
for i in range(1, 6):
    print((' ' * (5 - i)), end = '')
    print('*' * (i * 2 - 1))