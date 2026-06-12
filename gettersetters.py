from anyio import __value


class Myclass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"value is : {self._value}")




    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, new_value):
        self._value = new_value/10
        

obj = Myclass(10)    
print(obj._value)  # Output: 10
obj.show()  # Output: value is : 10
 


    