# 서버에서 바뀌는 데이터를 알아서 찾아서 반환
def test():
    yield 1
    yield 2 
    yield 3

x = test() # generator 생성 - 동적으로 바뀌는 데이터를 전달하며 종료

print(next(x))
print(next(x))
print(next(x))