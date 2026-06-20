import time

def usingfor():
    i = 0 
for i in range(1000):
        i = i + 1
        print(i)


def usingwhile():
    i = 0
    while i < 1000:
        i = i + 1
        print(i)

init = time.time()
usingfor()

t1 = time.time() - init

init = time.time()
usingwhile()
t2 = time.time() - init


print("Time taken by for loop: ", t1)
print("Time taken by while loop: ", t2)

#time.sleep

print("satyam")
time.sleep(5)
print("This is a message after 5 seconds")

#time.strftime()

t = time.localtime()
formated_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print("Current time: ", formated_time)
