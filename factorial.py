def factoriyal(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factoriyal(n - 1)

n = int(input("Enter a number: "))
print(factoriyal(n))