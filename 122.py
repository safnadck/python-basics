#Inheritance Class Polymorphism

# the child classes inherits the Vehicle methods

# Create a class called Vehicle and make
# Car, Boat, Plane child classes of Vehicle ?


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    pass

class Boat(Vehicle):

    def move(self):
        print("Sail!")


class Plane(Vehicle):

    def move(self):
        print("FLy!")


car1 = Car("Ford", "Mustang")  # Create a car class
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat class
plane1 = Plane("Boeing", "747")  #Create a Plane class


for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()