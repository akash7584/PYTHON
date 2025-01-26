def fact(p):
    f=1
    for i in range(1,1+p):
        f=f*i
        return f
n=int(input("Enter the Value of n="))
r=int(input("enter the value of p="))
nfact=fact(n)
n_rfact=fact(n-r)
npr=nfact//(n_rfact)
print("NPR Is=",npr)