# 5.Write a Python program that read a 3 digit number from user and perform the addition of their digits

num = int(input("Enter three digit no.:"))
sum = 0
while(num>0):
  dig = num%10
  sum = sum+dig
  num = num//10
print("The sum of the digit is:",sum)
