#Class Polymorphism

#Polymorphism is often used in Class methods,
# where we can have multiple classes with the same method name.

#Different classes with the same method ?


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive")


class Boat:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def move(self):
        print("Sail")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")




car1 = Car("Ford", "Mustang")  # Create a car class
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat class
plane1 = Plane("Boeing", "747")  #Create a Plane class

for x in (car1, boat1,plane1):
    x.move()


