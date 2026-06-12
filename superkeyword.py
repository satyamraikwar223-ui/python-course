class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class programmer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

satyam = programmer("Satyam", 50000, "Python")
harry = programmer("Harry", 60000, "Java")
print(satyam.name)
print(satyam.salary)
print(satyam.language)
print(harry.name)
print(harry.salary)
print(harry.language)
