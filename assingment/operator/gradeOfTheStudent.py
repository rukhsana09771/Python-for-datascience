# 7.Write a python program to display a greet message according to the marks obtained by the student.

marks = int(input("Enter your marks:"))
if(marks>=90 and marks<=100):
    print("Grade is:A")
elif(marks>=80 and marks<90):
    print("Grade is:B")
elif(marks>=70 and marks<80):
    print("Grade is:C")
elif(marks>=60 and marks<70):
    print("Grade is:D")
else:
   print("Grade:fail")
