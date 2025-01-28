# Create a class named Car.
# Use the __init__() function
# to assign values for make, model, and year.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

Car1 = Car("Toyota", "Innova", 2023)


print(Car1.make)
print(Car1.model)
print(Car1.year)