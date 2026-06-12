class Employee:
    name = "satyam"
    def __len__(self):
        i = 0
        for c in self.name:
            i += 1
        return i
    
e = Employee()
print(len(e))
print(e.name)

