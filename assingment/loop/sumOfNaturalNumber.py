# 6. Write a python program to find sum of all natural numbers between 1 to n.

num = int(input("Enter any natural number:"))
print("Sum of natural no. from 1 to ",num ,"are :")
sum = 0
while(num>0):
   sum=sum+num
   num-=1
print(sum)   