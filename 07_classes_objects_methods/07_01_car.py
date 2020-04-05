'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car:
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __str__(self):
        return f"{self.year} {self.model} is going at {self.max_speed} km/hr"

    def accel(self):
        self.max_speed += 5
        print(f"{self.year} {self.model} just accelerated!")

camry = Car("Camry", 2008, 60)
civic = Car("Civic", 2012, 75)
print(camry)
print(civic)
camry.accel()
camry.accel()
print(camry)
