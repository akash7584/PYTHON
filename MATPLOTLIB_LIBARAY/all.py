#matplotlib is a python libery for data visualization
# import matplotlib
# print(matplotlib._version_)
import numpy as np 
import matplotlib.pyplot as plt  
# xp=np.array([1,2,3,4,5,6])
# yp=np.array([10,20,30,40,50,60])
# plt.plot(xp,yp)
# plt.show()
# xp=np.array([1,2,3,4,5,6])
# yp=np.array([10,25,5,30,50,24])
# plt.plot(xp,yp)
# plt.show()
# xp=np.array([0,6])
# yp=np.array([0,250])
# plt.plot(xp,yp)
# plt.show()
#bydefault xaxis starat with 0
# yp=np.array([3,4,8,2,9,10])
# plt.plot(yp,marker='*')
# font1={'family':'serif','color':'yellow','size':20}
# font2={'family':'serif','color':'green','size':20}
# font3={'family':'serif','color':'red','size':30}
# plt.xlabel("X_axis_value",fontdict=font1)
# plt.ylabel("Y_axis_value",fontdict=font2)
# plt.title("My_Data",fontdict=font3)
# plt.show()


# yp=np.array([3,4,8,2,9,10])
# plt.plot(yp,'-.k')  #',-.,r'  marker=*  -. for line  y=for color
# # line style :(dot line) ->(dashed dot) --(dashed line)
# # color: (b=blue k=black)
# font1={'family':'serif','color':'yellow','size':20}
# font2={'family':'serif','color':'green','size':20}
# font3={'family':'serif','color':'red','size':30}
# plt.xlabel("X_axis_value",fontdict=font1)
# plt.ylabel("Y_axis_value",fontdict=font2)
# plt.title("My_Data",fontdict=font3)
# plt.show()
# yp=np.array([3,4,8,2,9,10])
# plt.plot(yp,marker='o',ms=20,mfc='k',mec='r')
#ms=marker size mfc=marker face color mec=marker edge color
# plt.show()
# ex=[1,2,3,4,5,6,7,8,9]
# salary=[6,8,10,12,14,15,16,18,23]
# plt.plot(ex,salary,marker='*' ,ms=10, mfc='y', mec='b',linestyle='--',linewidth=3)
# plt.xlabel("Experience")
# plt.ylabel("Salary")
# plt.title("Experience/salary")
# plt.grid(color='red',linestyle="-.",linewidth=2) # bydefalut grid(both axis)
# plt.show()

# ex=[1,2,3,4,5,6,7,8,9]
# salary=[6,8,10,12,14,15,16,18,23]
# plt.plot(ex,salary)
# plt.xlabel("Experience")
# plt.ylabel("Salary")
# plt.title("Experience/salary")
# plt.grid(axis='x') # bydefalut grid(both axis)
# plt.show()

# ex=[1,2,3,4,5,6,7,8,9]
# salary=[6,8,10,12,14,15,16,18,23]
# plt.plot(ex,salary)
# plt.xlabel("Experience")
# plt.ylabel("Salary")
# plt.title("Experience/salary")
# plt.grid(axis='y') # bydefalut grid(both axis)
# plt.show()
# first plot
# x1=[1,2,3,4,5,6]
# y1=[10,48,80,22,44,67]
# plt.subplot(2,3,1)
# plt.plot(x1,y1)


# # second plot
# x2=[1,2,3,4,5,6]
# y2=[101,480,80,221,44,607]
# plt.subplot(2,3,2)
# plt.plot(x2,y2)
# # plot three
# x3=[1,2,3,4,5,6]
# y3=[101,480,80,221,44,607]
# plt.subplot(2,3,3)
# plt.plot(x3,y3)

# x4=[1,2,3,4,5,6]
# y4=[10,48,80,22,44,67]
# plt.subplot(2,3,4)
# plt.plot(x4,y4)

# x4=[1,2,3,4,5,6]
# y4=[10,48,80,22,44,67]
# plt.subplot(2,3,5)
# plt.plot(x4,y4)

# x4=[1,2,3,4,5,6]
# y4=[10,48,80,22,44,67]
# plt.subplot(2,3,6)
# plt.plot(x4,y4)
# plt.show()
# all about pie chart
# import numpy as np 
# import matplotlib.pyplot as plt 
# company=np.array(['TCS','CTS','SAMSUNG','WIPRO','TECHMAHINDRA','OPTUM','MRF','AMAZON','GOOGLE'])
# placement=np.array([5,14,3,28,8,8,16,12,6])
# plt.pie(placement,labels=company)
# plt.title("My Collage Placment Record")
# plt.legend()
# plt.show()
# arr=np.array([0,0,1,1,0,0,1,0,0,1,2,3,1,0,5,4,2,1,0,3,0,4,1,2,4,3,4,
# 5,1,0,2,3,4,4,5,5,5,1,2,0,4,2,1,3,0,1])
# plt.hist(arr,5)
# plt.show()
# arr=np.random.uniform(1,5,100000)
# plt.hist(arr,100)
# print(arr)
# plt.show()