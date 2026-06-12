import time
t = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
hour = int(input("Enter the hour (0-23): "))

if (hour < 12 and hour > 0):
 print("Good Morning!")

elif (hour < 18 and hour >12):
 print("Good Afternoon!")
if (hour < 23 and hour > 18):
    print("Good Night!")