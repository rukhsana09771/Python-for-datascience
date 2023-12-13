# 13.	Write a python program to calculate sum of digits of a number.

num = int(input("Enter three digit no.:"))
sum = 0
while(num>0):
  dig = num%10
  sum = sum+dig
  num = num//10
print("The sum of the digit is:",sum)