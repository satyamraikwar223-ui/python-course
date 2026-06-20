# Hybrid Inheritance Example

from singleinheritance import cat, dog


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def showdetails(self):
        print(f"Vehicle Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
        self.type = "Car"

    def showdetails(self):
        print(f"{self.type} - Make: {self.make}, Model: {self.model}")

class Truck(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
        self.type = "Truck"

    def showdetails(self):
        print(f"{self.type} - Make: {self.make}, Model: {self.model}")

class HybridVehicle(Car, Truck):
    def __init__(self, make, model):
        super().__init__(make, model)
        self.type = "Hybrid Vehicle"

    def showdetails(self):
        print(f"{self.type} - Make: {self.make}, Model: {self.model}")

a1 = HybridVehicle("Toyota", "Prius")
a1.showdetails()

print(HybridVehicle.__mro__)  # Method Resolution Order

#heirarchical inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def showdetails(self):
        print(f"Animal Name: {self.name}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Dog"

    def showdetails(self):
        print(f"{self.type} - Name: {self.name}")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Cat"

    def showdetails(self):
        print(f"{self.type} - Name: {self.name}")

class dog1(Dog):
    def __init__(self, name):
        super().__init__(name)
        self.breed = "Labrador"

    def showdetails(self):
        print(f"{self.type} - Name: {self.name}, Breed: {self.breed}")


class cat1(Cat):
    def __init__(self, name):
        super().__init__(name)
        self.breed = "Siamese"

    def showdetails(self):
        print(f"{self.type} - Name: {self.name}, Breed: {self.breed}")


d1 = dog1("Buddy")
d1.showdetails()

c1 = cat1("Whiskers")
c1.showdetails()

print(dog1.__mro__)  # Method Resolution Order for dog1
print(cat1.__mro__)  # Method Resolution Order for cat1

 