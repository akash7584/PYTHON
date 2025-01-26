l=[]
sum=0
n=int(input("Enter how many seris"))
for i in range(n):
    val=int(input("Enter Value="))
    l.append(val)
for i in l:
    sum=sum+i
print("Sum is=",sum)