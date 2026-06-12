while True:
    a = input("Enter a number (or 'quit' to exit): ")
    if a == 'quit':
        break
    elif not a.isdigit():
        print("Please enter a valid number.")
        continue
    else: 

     for i in range(1, 11):

      print(a, "X", i, "=", int(a) * i)
