class Employee:
    def __init__(self , name ):
        self.name = name

    def showdetails(self):
        print(f"Employee Name is: {self.name}")


class Dancer:
    def __init__(self , dance):
        self.dance = dance

    def showdetails(self):
        print(f"Dance Style is: {self.dance}")


class DancerEmployee(Employee , Dancer):
    def __init__(self , name , dance):
        self.name = name
        self.dance = dance


d1 = DancerEmployee("Satyam" , "Hip Hop")
print(d1.name)
print(d1.dance)

print(DancerEmployee.mro())

print(Employee.showdetails(d1))

print(Dancer.showdetails(d1))