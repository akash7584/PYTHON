#SALARY AND BONUS DISTREBUTION:
Gender=str(input("Enter Your Gender="))
Salary=int(input("Enter Your Salary="))
if Gender=='Male' or Gender=='MALE' or Gender=='male':
    if Salary<50000:
        Bonus=Salary*10/100
    else:
        Bonus=Salary*15/100
elif Gender=='Female' or Gender=='FEMALE' or Gender=='female':
    if Salary<50000:
        Bonus=Salary*20/100
    else:
        Bonus=Salary*25/100
else:
    print("Invalid Input")
    Bonus=0
print("Your Bonus is=",Bonus,"Beause Your Gender is=",Gender)