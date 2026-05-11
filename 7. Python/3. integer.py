# 숫자를 할당하면 바로 int 타입의 변수가 됨
x = 5
y = 3

print(x + y)
print(x - y)
print(x / y)
print(x * y)

# 나머지
print(x % y)

# 제곱
print(x ** y)

# 진법 변환
x = 11
print(bin(x)) # 2진수
print(oct(x)) # 8진수
print(hex(x)) # 16진수

x = -10
print(abs(x)) # 절댓값

y = 4.21
print(y)
print(int(y)) # 소수의 정수 자리

z = '100'
print(z) # 숫자가 아닌 문자열
print(int(z))

# 비트 연산자 -> AND, OR, XOR, NOT
x = 5
y = 3
print(x & y) # x는 101 y는 011 -> 001
print(x | y) # x는 101 y는 011 -> 111
print(x ^ y) # x는 101 y는 011 -> 110 
print(~x) # x = 0(양/음수)0000101 -> ~x = 1111010 

print(x << 1) # 왼쪽으로 한 칸 이동 00000101 -> 00001010
print(x >> 1) # 오른쪽으로 한 칸 이동 00000101 -> 0000010