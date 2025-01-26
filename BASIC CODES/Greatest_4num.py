#Gratest between four number.
A=int(input("Enter 1st Number :"))
B=int(input("Enter 2nd Number :"))
C=int(input("Enter 3rd Number :"))
D=int(input("Enter 4th Number :"))
if(A>=B and A>=C and A>=D):
    print(A,"=A is Big number.")
elif(B>=A and B>=C and B>=D):
    print(B,"=B is Big Number.")
elif(C>=A and C>=B and C>=D):
    print(C,"=D is Big number.")
else:
    print(D,"=D is Big Number.")
