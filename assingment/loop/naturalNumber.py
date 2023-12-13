# 1. Write a python program to print all natural numbers from 1 to n. - using while loop

num = int(input("Enter any natural number:"))
print("The list of natural no. from 1 to ",num ,"are :")
i = 1
while(i<=num):
   print(i,end=", ")
   i+=1