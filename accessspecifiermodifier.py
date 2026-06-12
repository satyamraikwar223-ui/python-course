class Employee:
    def __init__(self):
        self.__name = "satyam" # private variable

a = Employee()
#print(a.__name) # this will give an error because __name is private and cannot be accessed directly from outside the class


print(a._Employee__name) # this will work because we are using name mangling to access the private variable

#protected access modifier
class Employee:
    def __init__(self):
        self._name = "satyam" # protected variable
a = Employee()
print(a._name) # this will work because we can access protected variable from outside the class but it is not recommended to do so

