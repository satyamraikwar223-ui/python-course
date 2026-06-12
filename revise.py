class Person():
    name ="satyam"
    age = 19
    state ="madhya pradesh"
    def info(self):
        print(f"name is : {self.name}, age : {self.age}, from : {self.state}")

p1 = Person()

p2 = Person()
p2.name = "satya"
p2.age = 19
p2.state = "madhya pradesh"

p3 = Person()
p3.name = "lakshya"
p3.age = 18
p3.state = "madhya pradesh"

p1.info()
p2.info()
p3.info()


class shape():
    def __init__(self, x  , y , z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return self.x * self.y * self.z
    
class cube(shape):
    def __init__(self, x):
        self.x = x
        super().__init__(x , x , x)

    def volume(self):
        return super().volume()
    
s = shape(5 , 10 , 15)
print(s.volume())

c = cube(5)
print(c.volume())
print(f"volume of cube is : {c.volume()}")


class cuboid(shape):
    def __init__(self, x , y , z):
        self.x = x
        self.y = y
        self.z = z
        super().__init__(x , y , z)

    def volume(self):
        return super().volume()
    
c1 = cuboid(5 , 10 , 15)
print(c1.volume())
print(f"volume of cuboid is : {c1.volume()}")

class circle(shape):
    def __init__(self, radius):
        self.radius = radius
        

    def circumference(self):
        return 2 * 3.14 * self.radius
    

c2 = circle(5)
print(c2.circumference())
print(f"circumference of circle is : {c2.circumference()}")

    
