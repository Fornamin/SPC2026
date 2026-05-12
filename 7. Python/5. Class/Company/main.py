# 여러 클래스를 불러서 조립해 실행
from employee import Employee
from person import Person
from driver import Driver

employee1 = Employee('James', 29, 'Samsung')
print(employee1.greet())
employee2 = Employee('John', 31, 'LG')
print(employee2.greet())
employee3 = Person('Amy', 24)
print(employee3.greet())
employee4 = Driver('Henry', 36, 'BMW')
print(employee4.greet())
print(employee4.drive())
print(employee4.get_name())