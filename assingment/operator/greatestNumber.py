# 6.Write a python program to find the greatest number among three.

num1 = int(input(print("Enter 1st no.:")))
num2 = int(input(print("Enter 2nd no.:")))
num3 = int(input(print("Enter 3rd no.:")))
if(num1 >= num2 & num1 >= num3):
    print("num1 is greater:",num1)
elif(num2 >= num1 & num2 >= num3):
    print("num2 is greater:",num2)
else:
    print("num3 is greater:",num3)