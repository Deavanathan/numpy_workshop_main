# find if the given number is a palindrome or not?
a=input("Enter the number:")

if a==a[::-1]:
    print("It is palindrome")
else:
    print("It is not a palindrome")