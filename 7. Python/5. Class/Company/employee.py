from person import Person

class Employee(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age) # inheritance
        self.company = company
    
    def greet(self): # method overriding
        return super().greet() + f' I work at {self.company}.'