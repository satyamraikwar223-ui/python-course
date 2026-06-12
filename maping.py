def cube(x):
    return x ** 3

l = [1, 2, 3, 4, 5]

#long way
 #newl = []
#for i in l:
 #   newl.append(cube(i))

 #by maping
newl = list(map(cube, l))
print(newl)

#by lambda function
newl = list(map(lambda x: x**3, l))
print(newl)

#filtering
def filter_function(x):
    return x>10

newnewl = list(filter(filter_function, l))
print(newnewl)

#by lambda function
newnewl = list(filter(lambda x: x>10, l))
print(newnewl)

#reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5]

sum = reduce(lambda x, y: x + y, numbers)
print(sum)
 