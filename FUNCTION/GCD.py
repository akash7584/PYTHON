#GCD=Greatest Common Divisor
def gcd(n1,n2):
    if n2!=0:
        return gcd(n2,n1%n2)
    else:
        return n1

Num1=int(input("Enter 1st number="))
Num2=int(input("Enter 2nd number="))
GCD=gcd(Num1,Num2)
print("GCD iS=",GCD)