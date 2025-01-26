#Calculate SPY number:
Number=int(input("Enter a number="))
sum=0
multiply=1
while Number!=0:
    lastdigit=Number%10
    sum+=lastdigit
    multiply*=lastdigit
    Number//=10
if sum==multiply:
    print("SPY Number")
else:
    print("Not SPY number")
print("Sum=",sum)
print("multiply=",multiply)


