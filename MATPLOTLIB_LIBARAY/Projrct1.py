import numpy as np
import matplotlib.pyplot as plt
#---------------------------------------------------------------------------
company=np.array(['TCS','JIO','TATA','CTS','GOOGLE','OPTAM','AMAZON','WIPRO','MRF','MICROSOFT'])
placement=np.array([8, 12, 5, 15, 10, 7, 13, 6, 9, 15])
plt.subplot(2,3,1)
plt.pie(placement,labels=company)
F={'family':'Georgia','color':'blue','size':20}
plt.title("Placement",fontdict=F)
plt.legend()


#-----------------------------------------------------------------
collage=np.array(['IITs','NITs','JADAVPUR','VIT','SRM','DTU','TECHNO','JIS','IEM','BRAINWARE'])
records=np.array([12, 8, 15, 10, 7, 13, 9, 6, 11, 9])
plt.subplot(2,3,2)
plt.pie(records,labels=collage)
F1={'family':'Georgia','color':'blue','size':20}
plt.title("Collages",fontdict=F1)
plt.legend()


#-----------------------------------------------------------------
place=np.array(['KOLKATA','HYDRABAD','JADAVPUR','PUNE','BENGALURU','MUMBAI','JAYPUR','BANARAS','CHANNAI','DELHI'])
score=np.array([8, 12, 15, 7, 10, 6, 14, 9, 11, 8])
plt.subplot(2,3,3)
plt.pie(score,labels=place)
F2={'family':'Georgia','color':'blue','size':20}
plt.title("Place",fontdict=F2)
plt.legend()

#-----------------------------------------------------------------
salary=np.array(['50000','60000','70000','80000','90000','100000','200000','150000','200000','250000'])
e=np.array([12, 5, 18, 7, 10, 15, 3, 9, 11, 10])
plt.subplot(2,3,4)
plt.pie(e,labels=salary)
F3={'family':'Georgia','color':'blue','size':20}
plt.title(" Salary",fontdict=F3)
plt.legend()



#----------------------------------------------------------------

place=np.array(['TATA,KOLKATA','WIPRO,HYDRABAD','TCS,JADAVPUR','SAMSUNG,PUNE','INFOSYS,BENGALURU','JIO,MUMBAI','GOOGLE,JAYPUR','MRF,BANARAS','MICROSOFT,CHANNAI','TECH,DELHI'])
score=np.array([14, 7, 12, 9, 8, 15, 10, 6, 11, 8])
plt.subplot(2,3,6)
plt.pie(score,labels=place)
F4={'family':'Georgia','color':'blue','size':20}
plt.title("Collage & Placement",fontdict=F4)
plt.legend()
plt.show()
