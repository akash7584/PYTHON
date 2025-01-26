# Number is divisible by 7 or 11
Num=int(input("Enter Any Number :"))
if(Num%7==0 and Num%11!=0):
    print(Num,"Divisible By 7 ")
elif(Num%11==0 and Num%7!=0):
    print(Num,"Divisible By 11")
elif(Num%7==0 and Num%11==0):
    print(Num,"Devisible by both")
else:
    print(Num,"Not devisible by 7 or 11")