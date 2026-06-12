class Math:
    def __init__(self , num): #constructor
        self.num = num

    def addtonum(self , x):
        self.num = self.num + x

#static method is a method that belongs to the class rather than an instance of the class. It can be called on the class itself, rather than on an instance of the class. Static methods are defined using the @staticmethod decorator.
#Static methods do not have access to the instance (self) or class (cls) variables. They are used for utility functions that do not require access to the instance or class variables.  
    @staticmethod

    def add(x , y):
        return x + y
#Example of using static method
print(Math.add(5 , 10)) #Output: 15

a = Math(5)
print(a.num) #Output: 5
a.addtonum(10)
print(a.num) #Output: 15

