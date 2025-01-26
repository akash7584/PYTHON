import pandas as pd
df=pd.read_csv('C:\\XboxGames\\GameSave\student.csv')

#head() by default returns the first 5 rows of the DataFrame
print(df.head())

#tail() by default returns the last 5 rows of the DataFrame
print(df.tail())
print(df[2:5])

