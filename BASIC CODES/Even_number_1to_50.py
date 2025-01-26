#write a programe print all even number within 1 to 50
Number=int(input("Enter a number(ending point)="))
for i in range(1,Number):
    if i%2==0:
        print(i)