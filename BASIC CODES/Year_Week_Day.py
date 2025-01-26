#convert specified days into years, weeks and days
Day=int(input("Enter Any days :"))
Year=Day//365
Rem_Days=Day%365
Week=Day//7
Rem_Days=Day%7
print("Year is :",Year)
print("Week is :",Week)
print("Rem_Days is :",Rem_Days)