# #8. Enter basic salary from the user. Write a program to calculate DA and HRA on the following conditions:-
# Salary	DA	HRA
# <=2000	10%	20%
# >2000 && <=5000	20%	30%
# >5000 && <=10000	30%	40%
# >10000	50%	50%

salary = int(input("Enter basic salary of the user:"))
if(salary<=2000):
    DA =  (salary*10)/100
    HRA = (salary*20)/100
    print("DA:",DA)
    print("HRA:",HRA)

elif(salary>2000 and salary<=5000):
    DA =  (salary*20)/100
    HRA = (salary*30)/100
    print("DA:",DA)
    print("HRA:",HRA)

elif(salary>5000 and salary<=10000):
    DA =  (salary*30)/100
    HRA = (salary*40)/100
    print("DA:",DA)
    print("HRA:",HRA)

elif(salary>10000):
    DA =  (salary*50)/100
    HRA = (salary*50)/100
    print("DA:",DA)
    print("HRA:",HRA)