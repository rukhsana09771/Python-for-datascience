# 12. Write a python program to find sum of first and last digit of a number.

num = int(input("Enter any number:"))
count = 0
while(num!=0):
    if(count==0):
        last = num%10
        count = count+1
    first = num%10
    num = num//10
sum = first + last
print("sum of first and last digit are:",sum)        