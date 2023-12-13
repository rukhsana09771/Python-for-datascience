# 2. Write a python program to print all natural numbers in reverse (from n to 1). - using while loop

num = int(input("Enter any natural number:"))
print("The reverse of natural no. from 1 to ",num ,"are :")
i = 1
while(i<=num):
   print(num,end=" ")
   num=num-1
   