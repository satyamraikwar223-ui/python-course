class Employee:
    company = "Apple"
    def show(self):
        print(f"The name of employee is {self.name} and company is {self.company}")


    
    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Satyam"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)

# As alternative constructor
class Employee:
    def __init__(self, name, company):
        self.name = name
        self.company = company
@classmethod
def fromStr(cls, string):
    return cls(string.split("-")[0], string.split("-")[1])

e2 = Employee.fromStr("satyam-Apple")
print(e2.name)
print(e2.company)

string = "satya-google"
e3 = Employee.fromStr(string)
print(e3.name)
print(e3.company)
