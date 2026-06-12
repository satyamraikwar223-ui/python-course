class animal:
    def __init__(self , name ):
        self.name = name

    def make_sound(self):
        print("Animal makes a sound")


class dog(animal):
    def __init__(self, name):
        super().__init__(name)
        

    def make_sound(self):
        print("Dog barks")

d1 = dog("Buddy")
d1.make_sound()

a1 = animal("Generic Animal")
a1.make_sound()
class animals:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Animals makes a sound")


class cat(animals):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Cat meows")


c1 = cat("Whiskers")
c1.make_sound()

a2 = animals("Generic Animals")
a2.make_sound()
