def factorial(n):
    if n<2:
        return 1
    return n*factorial(n-1) #1000 times max
print(factorial(10)) # if 1000 then error