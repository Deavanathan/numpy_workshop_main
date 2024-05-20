#write a program to find if the given number is prime no or not
a=int(input("Enter the number: "))
flag=0
for i in range(2,int(a/2)):
    if i%a==0:
        flag=1
        break
    else:
        continue
    
if(flag==0):
    print("It is a prime number")
else:
    print("It is not a prime number")