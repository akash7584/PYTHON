import numpy as np
import matplotlib.pyplot as plt
company=np.array(['TCS','JIO','TATA','CTS','GOOGLE','OPTAM','AMAZON','WIPRO','MRF'])
placement=np.array([5,14,3,28,8,8,16,12,6])
plt.pie(placement,labels=company)
plt.title("PLacement Records")
plt.legend()
plt.show()