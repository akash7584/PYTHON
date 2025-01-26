#রেকার্শন হল = ফাংশন টাকে সে ততক্ষণ কল করবে যতক্ষণ তার বেস(0,1 ) কন্ডিশন এ না আসে। 
# def fact(p):
#     if p==0:
#         return 1
#     elif p==1:
#         return 1
#     else:
#         return p*fact(p-1)
# Num=int(input("Enter Any number="))
# factorial=fact(Num)
# print("Factorial=",factorial)
def sum(p):
    if p==0:
        return 0
    elif p==1:
        return 1
    else:
        return p+sum(p-1)
Num=int(input("Enter any number="))
SUM=sum(Num)
print("SUM IS=",SUM)