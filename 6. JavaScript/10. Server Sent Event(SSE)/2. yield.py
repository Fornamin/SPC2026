# 서버에서 바뀌는 데이터를 알아서 찾아서 반환
def test():
    print('A') # 함수의 수행할 작업
    yield 1 # yield를 실행하고 멈춤
        
    print('B')
    yield 2 
        
    print('C')
    yield 3

x = test() # generator 생성 - 동적으로 바뀌는 데이터를 전달하며 종료
try:
    while True:
        print(next(x))
except StopIteration:
    print('all data is printed')