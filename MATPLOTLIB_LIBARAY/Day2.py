import numpy as np
import matplotlib.pyplot as plt

xp=np.array([2,3,4,5,7,10])
yp=np.array([600000,800000,1200000,1300000,1400000,3300000])
plt.subplot(3,3,1)
plt.plot(xp,yp,marker='*',mec='b')
plt.plot(xp,yp)
font1={'family':'serif','color':'r','size':7}
font2={'family':'serif','color':'r','size':7}
font3={'family':'serif','color':'r','size':10}
plt.xlabel("experience",fontdict=font1)
plt.ylabel("salary",fontdict=font2)
plt.title("salary bast an exp",fontdict=font3)
plt.grid(color='red')


# y=np.array([8,19,3,7,46,18])
# x=np.array([2019,2020,2021,2022,2023,2024])
# plt.subplot(3,3,2)
# plt.plot(x,y,'*--g')
# f1={'family':'serif','color':'b','size':7}
# f2={'family':'serif','color':'b','size':7}
# f3={'family':'serif','color':'b','size':10}
# plt.xlabel("TCS",fontdict=f1)
# plt.ylabel("year",fontdict=f2)
# plt.title("year/TCS",fontdict=f3)
# plt.grid(color='k')

# x=np.array(['TCS','TATA','WIPRO','SAMSUNG','PW','OPTUM'])
# y=np.array([10,5,19,3,7,10])
# plt.subplot(3,3,3)
# plt.plot(x,y,'*--k')
# f1={'family':'serif','color':'b','size':7}
# f2={'family':'serif','color':'b','size':7}
# f3={'family':'serif','color':'b','size':10}
# plt.xlabel("company",fontdict=f1)
# plt.ylabel("highar",fontdict=f2)
# plt.title("company/highar-2024",fontdict=f3)
# plt.grid(color='g')

# x=np.array(['TCS','TATA','WIPRO','SAMSUNG','PW','OPTUM'])
# y=np.array([1000000000,20000000,900000000,230000000,500000000,1500000000])
# plt.subplot(3,3,4)
# plt.plot(x,y,'*--g')
# f1={'family':'serif','color':'b','size':7}
# f2={'family':'serif','color':'b','size':7}
# f3={'family':'serif','color':'b','size':10}
# plt.xlabel("company",fontdict=f1)
# plt.ylabel("stock",fontdict=f2)
# plt.title("company/stock-2024",fontdict=f3)
# plt.grid(color='b')

# x=np.array(['TCS','TATA','WIPRO','SAMSUNG','PW','OPTUM'])
# y=np.array([30,8,91,3,90,19])
# plt.subplot(3,3,5)
# plt.plot(x,y,'*--g')
# f1={'family':'serif','color':'b','size':7}
# f2={'family':'serif','color':'b','size':7}
# f3={'family':'serif','color':'b','size':10}
# plt.xlabel("company",fontdict=f1)
# plt.ylabel("developer",fontdict=f2)
# plt.title("company/developer-2024",fontdict=f3)
# plt.grid(color='pink')

# x=np.array(['TCS','TATA','WIPRO','SAMSUNG','PW','OPTUM'])
# y=np.array([71,13,33,65,7,80])
# plt.subplot(3,3,6)
# plt.plot(x,y,'*--g')
# f1={'family':'serif','color':'b','size':7}
# f2={'family':'serif','color':'b','size':7}
# f3={'family':'serif','color':'b','size':10}
# plt.xlabel("company",fontdict=f1)
# plt.ylabel("CSE",fontdict=f2)
# plt.title("company/CSE-2024",fontdict=f3)
# plt.grid(color='y')

# x=np.array(['TCS','TATA','WIPRO','SAMSUNG','PW','OPTUM'])
# y=np.array([1000000000,20000000,900000000,230000000,500000000,1500000000])
# plt.subplot(3,3,7)
# plt.plot(x,y,'*--g')
# f1={'family':'serif','color':'b','size':7}
# f2={'family':'serif','color':'b','size':7}
# f3={'family':'serif','color':'b','size':10}
# plt.xlabel("company",fontdict=f1)
# plt.ylabel("stock",fontdict=f2)
# plt.title("company/stock-2024",fontdict=f3)
# plt.grid(color='b')

# x=np.array(['TCS','TATA','WIPRO','SAMSUNG','PW','OPTUM'])
# y=np.array([30,8,91,3,90,19])
# plt.subplot(3,3,8)
# plt.plot(x,y,'*--g')
# f1={'family':'serif','color':'b','size':7}
# f2={'family':'serif','color':'b','size':7}
# f3={'family':'serif','color':'b','size':10}
# plt.xlabel("company",fontdict=f1)
# plt.ylabel("developer",fontdict=f2)
# plt.title("company/developer-2024",fontdict=f3)
# plt.grid(color='pink')

# x=np.array(['TCS','TATA','WIPRO','SAMSUNG','PW','OPTUM'])
# y=np.array([71,13,33,65,7,80])
# plt.subplot(3,3,9)
# plt.plot(x,y,'*--g')
# f1={'family':'serif','color':'b','size':7}
# f2={'family':'serif','color':'b','size':7}
# f3={'family':'serif','color':'b','size':10}
# plt.xlabel("company",fontdict=f1)
# plt.ylabel("CSE",fontdict=f2)
# plt.title("company/CSE-2024",fontdict=f3)
# plt.grid(color='y')

plt.show()