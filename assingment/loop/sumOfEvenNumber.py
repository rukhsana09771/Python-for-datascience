# 7. Write a python program to find sum of all even numbers between 1 to n.

num = int(input('Enter any natural number:'))
sum = 0
for i in range(num):
    if(i%2==0):
        print(i)
        sum+=i
print("Sum of even no. from 1 to ",num ,"are :",sum)        