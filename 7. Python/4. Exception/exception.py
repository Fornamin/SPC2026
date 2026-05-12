# 기존의 경우 예외 처리를 전부 if 문으로 구현
# 일단 실행하고 에러가 발생하면 예외 처리를 하고 다음 코드를 진행
# raise: 에러를 강제 유발 -> custom 예외 처리 가능

try:
    result = 10 / 0 # zero definition error
except ZeroDivisionError:
    print('You can not divide a num by 0')
except:
    print('Unknown error')
print('------------------ Proceed ------------------')

try:
    num = int('Hello')
except ValueError:
    print('You can not convert string into number')
print('------------------ Proceed ------------------')

list = [1, 2, 3]
try:
    list[3]
except IndexError:
    print('Index out of range')
print('------------------ Proceed ------------------')

try:
    with open('unknown.txt', 'r') as file:
        data = file.read()
except FileNotFoundError:
    print('File does not exist')