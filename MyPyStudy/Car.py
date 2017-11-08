class Car:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        print(self.name)


my_car = Car("audi")
my_car.get_name()