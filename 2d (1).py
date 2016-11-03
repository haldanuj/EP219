
import numpy as np
import matplotlib.pyplot as plt
import math


file=open('recoilenergydata_EP219.csv','r')
#defined list to store the values of log(L(s))
y=[]    

#here defined log(L) function with s as parameter(sigma)
def likelihood(s):
	
	file=open('recoilenergydata_EP219.csv','r')
	i=0
	sum1=0				
	sum2=0
	sum3=0
	sum4=0

	while i<40:
		if i<5:
			[Er, Events]=file.readline().split(',')
			 
			m1= float(Events)
			n1=float(Er)
			n2=1000*(np.exp(-n1/10))
			m2=np.log(n2)
			sum1=sum1+(-n2 +m1*m2)  
			#sum1=summation of (-Bi + Di*log(Bi)) where Bi are backgound events and Di are 
			#observed events for 0<i<5

		elif 5<=i<=15:
			[Er, Events]=file.readline().split(',')
			 
			n1=float(Er)
			m1= float(Events)
			n2=1000*(np.exp(-n1/10))
			t=s*20*(n1-5) 
			n3=t+n2
			m2=np.log(n3)
			sum2 =sum2 + (-n3 + m1*m2)
			#sum2=summation of (-(Bi+Ti) + Di*log(Bi+Ti)) where Bi are backgound events,Di are 
			#observed events and Ti are observed events for 5<=i<15

			
		elif 15<i<25:
			[Er, Events]=file.readline().split(',')
			
			n1=float(Er)
			m1= float(Events)
			n2=1000*(np.exp(-n1/10))
			t=s*20*(25-n1) 
			n3=t+n2
			m2=np.log(n3)
			sum3 =sum3 + (-n3 + m1*m2)
			
			#sum3=summation of (-(Bi+Ti) + Di*log(Bi+Ti)) where Bi are backgound events,Di are 
			#observed events and Ti are observed events for 15<=i<25
		
		else :
			[Er, Events]=file.readline().split(',') 
			
			m1= float(Events)
			n1=float(Er)
			n2=1000*(np.exp(-n1/10))
			m2=np.log(n2)
			sum4 =sum4 + (-n2 + m1*m2)
			#sum4=summation of (-Bi + Di*log(Bi)) where Bi are backgound events and Di are 
			#observed events for 25<i<40

		i=i+1

	return (sum1 +sum2+sum3+sum4)


s=np.linspace(0, 1, 100) 
y= likelihood(s)

fig, ax = plt.subplots()
ax.plot(s, y)

plt.title('Likelihood plot')
plt.xlabel('sigma')
plt.ylabel('log(sigma)')
plt.show()




