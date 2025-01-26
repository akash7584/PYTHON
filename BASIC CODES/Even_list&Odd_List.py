#List=[1,3,4,2,6,8,9]- Even_List=[4,2,6,8]-Odd_list=[1,3,9]
List=[]
Even_Element=[]
Odd_Element=[]
Size=int(input("Enter How Many Seris Are input="))
for i in range(Size):
    val=int(input("Enter Element Value ="))
    List.append(val)
print("Your List Is =",List)
for i in range(Size):
    if List[i]%2==0:
        Even_Element.append(List[i])
print("Even Element is =",Even_Element)
for i in range(Size):
    if List[i]%2!=0:
        Odd_Element.append(List[i])
print("Odd Element is=",Odd_Element)