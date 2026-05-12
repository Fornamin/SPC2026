class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, value):
        self.age = value

    def greet(self):
        return f'Hello, I\'m {self.name} and {self.age} years old.'