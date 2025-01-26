Num=int(input("Enter a number="))
sum=0
while Num!=0:
    R=Num%10
    sum=sum*10+R
    Num=Num//10
print("Reverse",sum)    



