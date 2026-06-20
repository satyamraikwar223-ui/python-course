#e1
a = True 
print(a:=True)

#e2
number = [1,2,3,4,5]

while (n := len(number)) > 0:
    print(number.pop())

#e3
#normal loop
#food = list()
#while True:
#    item = input("Enter a food: ")
#    if item == "quit":
#        break
#    food.append(item)

#using walrus operator
food = list()
while (item := input("Enter a food: ")) != "quit":
    food.append(item)
    


