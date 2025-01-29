
import matplotlib.pyplot as plt
company=np.array(['TCS','JIO','TATA','CTS','GOOGLE','OPTAM','AMAZON','WIPRO','MRF','MICROSOFT','INNOVA','PULSE','TECHFLOW','TECHTIDE','NOVACORE'])
placement=np.array([8, 4, 6, 7, 5, 3, 10, 11, 6, 9, 2, 7, 6, 9, 7])
plt.subplot(2,2,1)
plt.pie(placement,labels=company)
plt.title("Placement")
plt.legend()
plt.show()