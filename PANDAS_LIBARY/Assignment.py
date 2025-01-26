import pandas as pd

# 1st>   Show all Student Record.
show=pd.read_csv('MY_EMPLOYEE_DATA.csv')
print(show)

# 2nd>   Show only Jadavpur or Shibpur Students Records.
show_collage_student=show[(show['COLLAGE']=='Jadavpur')| (show['COLLAGE']=='Shibpur')]
print("After Show Only Jadavpur or Shibpur Students Records")
print(show_collage_student)

# 3rd>   Show Those student Records imformation Who Placed In Capsamini and Salary Graterthen 700000
print("After Show Those student Who Placed In Capsamini and Salary Graterthen 700000")
placed_salary=show[(show['PLACEMENT']=='Capsamini') & (show['SALARY']>700000)]
print(placed_salary)

# 4th>   Show all students whose job location hydrabad.
print("After Printing Whose students job location is hydrabad ")
job_location=show[(show['JOB-LOCATION']=='Hydrabad')]
print(job_location)

# 5th>   Show all students records whose location hydrabad or mumbai and salary graterthen 900000.
print("After Printing Show all students records whose location hydrabad or mumbai and salary graterthen 900000")
location_salary=show[((show['JOB-LOCATION']=='Hydrabad') | (show['JOB-LOCATION']=='Mumbai')) & (show['SALARY']>900000)]
print(location_salary)