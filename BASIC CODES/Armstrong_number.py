num=int(input("Enter a Number="))
Temp=num
temp1=Temp
count=0
Arms=0
while num!=0:
    count+=1
    num=num//10 
while Temp!=0:
    Reverse=Temp%10
    Arms=Arms+Reverse**count
    Temp=Temp//10
print(Arms)
if Arms==temp1:
    print("This is Armstrong Number")
else:
    print("Not Armstrong Number")

