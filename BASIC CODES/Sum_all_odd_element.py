l=[]
sum=0
n=int(input("Enter how many seris"))
for i in range(n):
    val=int(input("Enter Value="))
    l.append(val)
for i in range(n):
    if i%2==1:
        sum=sum+l
print("Sum is=",sum)
