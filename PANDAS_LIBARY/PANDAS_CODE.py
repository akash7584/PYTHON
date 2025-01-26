import pandas as pd
# l=[['1','argha','btech',35000],['2','akash','btech',35000],['3','arpan','btech',35000],['5','prince','btech',35000],['5','palash','btech',35000]]
# db=pd.DataFrame(l,columns=['sl','name','dept','fees'])
# print(db)
Employee={'name':['akash','argaa','prince','palash','arijit'],
          'id':['10','20','30','40','50'],
          'office':['tcs','tata','ninja','ardent','wipro'], 
          'location':['kolkata','pune','gurugram','hydrabad','bengaluru'],
          'salary':[70000,65000,50000,80000,55000]}   

show=pd.DataFrame(Employee)
show.to_csv('sky.csv')
df=pd.read_csv('data.csv')
print(df)