# import matplotlib

 # cheak Version.
# print(matplotlib.__version__)
import numpy as np
import matplotlib.pyplot as plt
xp=np.array([2,3,4,5,6,7,10])
yp=np.array([6,8,12,15,15,16,33])
plt.plot(xp,yp)
t={'family':'serif','color':'blue','size':20}
t1={'family':'serif','color':'green','size':20}
t2={'family':'serif','color':'red','size':30}
plt.xlabel("Year_Experiance",fontdict=t)
plt.ylabel("Year_Experiance",fontdict=t1)
plt.title("Salary_Based_Experience",fontdict=t2)
plt.show()

