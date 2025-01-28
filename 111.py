#Python Inheritance

#Inheritance allows us to define a class that inherits all the methods
# and properties from another class.

#Parent class is the class being inherited from, also called base class.

#Child class is the class that inherits from another class,
# also called derived class.

#Create a Parent Class

#Create a class named Person,
# with firstname and lastname properties, and a printname method:


class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname

    def printname(self):
        print(self.firstName, self.lastName)


#use the person class to create an object,
# and then execute the printname methode:



x = Person("john", "Doe")
x.printname()






#create a aclass named student


class Student:
    pass





x = Student("Mike", "olsen")
x.printname()