class Animal:
    def __init__(self , name , species):
        self.name = name
        self.species = species

    def showdetails(self):
        print(f"{self.name} is a {self.species}")

class dog(Animal):
    def __init__(self, name , breed):
        super().__init__(name , species = "Dog")
        self.breed = breed

    def showdetails(self):
        super().showdetails()
        print(f"{self.name} is a {self.breed}")


class pug(dog):
    def __init__(self, name , color):
        super().__init__(name , breed = "Pug")
        self.color = color

    def showdetails(self):
        super().showdetails()
        print(f"{self.name} is a {self.color} Pug")


p1 = pug("Buddy" , "black")
p1.showdetails()

print(pug.mro())

print(Animal.showdetails(p1))

print(dog.showdetails(p1))

print(pug.showdetails(p1))