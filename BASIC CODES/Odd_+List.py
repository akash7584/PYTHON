#Odd Number print
l=[]
n=int(input("Enter how many seris"))
for i in range(n):
    val=int(input("Enter Value="))
    l.append(val)
for i in range(n):
    if i%2==1:
        print(l[i])
#Even Number print
l=[]
n=int(input("Enter how many seris"))
for i in range(n):
    val=int(input("Enter Value="))
    l.append(val)
for i in range(n):
    if i%2==0:
        print(l[i])

