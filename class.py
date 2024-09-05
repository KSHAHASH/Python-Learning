#Class in PYTHON


class Person:
    def __init__(self, first_name, last_name): #this is a constructor
        self.first_name = first_name
        self.last_name = last_name

    def talk(self):
        print("Please talk")


shahash = Person("shahash", "kandel")
print(shahash.first_name)
shahash.talk()


#one more exercise in class

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self. year = year

    def get_info(self):
        print(f"The car is {self.make} model of {self.model} and year {self.year} ")

vehicle_1 = Car("Honda", "Accord", 2020)
vehicle_1.get_info()
print(vehicle_1.model)





