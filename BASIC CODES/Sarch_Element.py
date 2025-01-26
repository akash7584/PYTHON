list=[]
Size=int(input("Enter How Many Seris Are input="))
for i in range(Size):
    val=int(input("Enter Element Value ="))
    list.append(val)
print("Your List Is =",list)
sarch=int(input("Enter sarch element="))
x=list.count(sarch)
print("Sarch element count is =",x)
