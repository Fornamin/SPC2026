def add_num(a, b):
    return a + b

print('두 수의 합은', add_num(3, 4))

def add_num2(a, b):
    return a, b, a + b # 여러 인자를 동시에 반환 가능 -> tuple에 담겨서 옴
x, y, sum = add_num2(4, 3)
print(f'{x} + {y} = {sum}')

def calc(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b

    return addition, subtraction, multiplication, division
add, sub, mul, div = calc(432, 564)
print(f'add: {add}, sub: {sub}, mul: {mul}, div: {div}')
print('-' * 50)

add, _, mul, _ = calc(104, 439)
print(f'add: {add}, mul: {mul}')
print('-' * 50)

def create_profile(name, age, city = '서울', job = '학생'):
    profile = f'Name: {name}, Age: {age}, City: {city}, job: {job}'
    return profile

print(create_profile('홍길동', 24, '부산'))
print(create_profile('김민정', 25, job = '직장인'))

