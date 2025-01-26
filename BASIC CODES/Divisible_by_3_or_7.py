#Those Elements Whitch Are Divisible By 3 and 7 
list=[]
Num=int(input("Enter how many seris= "))
for i in range(Num):
    val=int(input("Enter Value= "))
    list.append(val)
print("LIST IS =",list)
for i in range(Num):
    if list[i]%3==0 and list[i]%7==0:
        print(list[i],"=This Number Divisible By 3 And 7")