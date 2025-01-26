#Calculate triangle value:
A=int(input("Enter 1st Angle="))
B=int(input("Enter 2nd Angle="))
C=int(input("Enter 3rd Angle="))
sum=A+B+C
if sum==180: 
    print("This Is Triangle=",sum)
else:
    print("Not triangle=",sum)