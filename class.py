class Person:
    name = "satyam"
    age = 19
    state = "madhya pradesh"
    def info(self):
       print(f"Name is : {self.name}, Age : {self.age}, from: {self.state}") 

p1 = Person()
#p1.name = "satya"
#p1.age = 19
#p1.state = "madhya pradesh"

p2 = Person()
p2.name = "lakshya"
p2.age = 18
p2.state = "madhya pradesh"

p1.info()

p2.info()