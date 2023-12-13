# 10. Write a python program to count number of digits in a number.

num = int(input("Enter any number:"))
cout=0
while(num>0):
    n = num%10
    cout=cout+1
    num=num//10
print("Number of digit are:",cout)    
