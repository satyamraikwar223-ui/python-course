dict = {"satyam" : 73,
        "lakshya" : 80.4,
        "suraj" : 78,
        "neeraj" : 91,
        "adarsh" : 80}

while True:
    n = input("\nEnter the name of student (or type 'exit' to stop): ")
    
    if n.lower() == 'exit':
        print("Program closed.")
        break
        
    if n in dict:
        print("The percentage of", n, "is", dict[n])
    else:
        print("The name of student is not found in the dictionary.")
