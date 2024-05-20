#write a program to find the factorial of a nummber
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    

n=int(input("Enter the number:"))

print(factorial(n))