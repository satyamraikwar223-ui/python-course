class Employee:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])


if __name__ == "__main__":
    e1 = Employee.fromstr("satyam-Apple")
    print(e1.name)
    print(e1.company)


    string = "satya-google"
    e2 = Employee.fromstr(string)
    print(e2.name)
    print(e2.company)
 

 
