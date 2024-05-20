#write a program to find the sum of digits of a given number'
a = int(input("Enter the number:"))

sum = 0
while a > 0:
        
    digit = a % 10
    sum = sum + digit
    a = a // 10
print("The Sum of digits is : ", sum)