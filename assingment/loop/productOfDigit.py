# 14.	Write a python program to calculate product of digits of a number.

num = int(input("Enter three digit no.:"))
product = 1
while(num>0):
  dig = num%10
  product = product*dig
  num = num//10
print("The product of the digit is:",product)