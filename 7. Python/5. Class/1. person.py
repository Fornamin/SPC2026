class Person: # Class -> 속성(attribute)과 함수(function)로 무언가를 정의
    def __init__(self, name, age):
        # Class Instantiation
        # 객체를 생성할 때 처음 호출됨
        # 첫 번째 인자는 self -> 변경 가능하지만 보통 self(자기 자신)를 사용
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hello, I\'m {self.name}')

    def study(self, subject):
        print(f'{self.name} is studying {subject}')
        
person1 = Person('Alice', 25)
person2 = Person('Bob', 29)

person1.greet();
person2.greet();
person1.study('Python');
person2.study('C');