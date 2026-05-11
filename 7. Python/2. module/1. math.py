import math
print(math.pi)
print(math.e)
print(math.sqrt(16))
print('-' * 50)

from datetime import datetime as dt
# 날짜 생성
a = dt(2024, 1, 1, 0, 0, 0)
b = dt.now()

print(a)
print(b)

# 날짜 차이 계산
diff = b - a

print("날짜 차이:", diff)
print("총 일수:", diff.days)

# 현재 시간
now = dt.now()
print("현재 시간:", now)

# 문자열 포맷팅
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("포맷된 시간:", formatted)
print('-' * 50)

import random
print(random.random())
print(math.floor(random.random() * 100)) #  0 <= x < 100
print(random.randint(1, 100)) # 1 <= x < 100
print('-' * 50)

def rollDice():
    n = random.randint(1, 6)
    return n
for i in range (0, 5):
    print('My dice num is' , rollDice())
print('-' * 50)

fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'peace', 'pineapple']
def pickFruit(): 
    num = random.randint(0, len(fruits) - 1)
    return fruits[num]
for i in range(0, 5):
    print('My fruit is', pickFruit())
print('-' * 50)

def pickFruit2():
    return random.choice(fruits)
for i in range(0, 5):
    print('My fruit is', pickFruit2())