
import numpy as np
import matplotlib.pyplot as plt
import math

file=open('recoilenergydata_EP219.csv','r')

x= []
N= []
num_bins=40
i=0
while i<40:

	# for i<5 only background events contribute in total no. of events
	if i<5:
		[Er, Events]=file.readline().split(',')
		x.append(float(Er))
		n1=float(Er)
		n2=1000*(np.exp(-n1/10))
		N.append(n2)		
		
	elif 5<=i<15:
		[Er, Events]=file.readline().split(',')
		x.append(float(Er))
		n1=float(Er)
		n2=1000*(np.exp(-n1/10))	#n2 gives total no of background events
		n3=0.01*20*(n1-5) 			#n3 gives total no of expected events for given sigma here sigma=0.01
		n4=n3+n2
		N.append(n4)		
		

	elif 15<=i<25:
		[Er, Events]=file.readline().split(',')
		x.append(float(Er))
		n1=float(Er)
		n2=1000*(np.exp(-n1/10))	#n2 gives total no of background events
		n3=0.01*20*(25-n1) 			#n3 gives total no of expected events for given sigma ,here sigma=0.01
		n4=n3+n2
		N.append(n4)		
		
	#for i>25 only background events contribute in total no. of events
	else :
		[Er, Events]=file.readline().split(',')
		x.append(float(Er))
		n1=float(Er)
		n2=1000*(np.exp(-n1/10))
		N.append(n2)		
	i=i+1


width=1.0
pos = np.arange(len(x))
plt.figure()
plt.title('Histogram of Background  data and expected data')
plt.xlabel('Measured recoil energies(Kev)')
plt.ylabel('No. of events')
plt.bar(pos, N, width, color='r')
plt.text(30,18000,'Sigma=100fb')
plt.show()








