from person import Person
class Driver(Person):
    def __init__(self, name, age, car):
        super().__init__(name, age)
        self.car = car

    def drive(self):
        return f'{self.name} starts to drive {self.car}.'