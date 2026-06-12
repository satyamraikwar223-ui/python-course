class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def showdetails(self):
        print(f"Employee Name is: {self.name}, His ID: {self.id}, work at Salary: {self.salary}")



 # Inheritance
class Programmer(Employee):
    def showlanguage(self):
        print("the default language is python")
    


 #e1 = Employee("Satyam", 101, 50000)   
e1 = Programmer("Satyam", 101, 50000)
e1.showdetails()
e1.showlanguage()

