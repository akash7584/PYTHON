Num=int(input("Enter a Number="))
temp=Num
sum=0
while Num!=0:
    Reverse=Num%10
    sum=sum*10+Reverse
    Num=Num//10
print("reverse",sum)                                   
if sum==temp:
    print("palindrom ")
else:
    print("not palindeom")  
