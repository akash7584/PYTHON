import pandas as pd
df=pd.read_csv('akash.csv')
#Statistical information about the data
print("Maximum salary=",df['Salary'].max())
print("Minimum salary=",df['Salary'].min())


#print those employee records whose salary is less than 30000
print(df[df['Salary']<30000])


#print all imformation who getting maximum And minimum salary
print(df[df['Salary']==df['Salary'].max()])
print(df[df['Salary']==df['Salary'].min()])
