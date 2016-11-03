
import numpy as np
import matplotlib.pyplot as plt
import math

file=open('recoilenergydata_EP219.csv','r')


x= []
y =[]
N= []


num_bins=40
i=0
while i<40:

	[Er, Events]=file.readline().split(',')
	x.append(float(Er))
	y.append(float(Events)) 
	n1=float(Er)
	n2=1000*(np.exp(-(n1)/10)) 
	N.append(n2)		
	i=i+1

width=1.0
pos = np.arange(len(x))
plt.figure()
plt.title('Histogram of Background  data')
plt.xlabel('Measured recoil energies(Kev)')
plt.ylabel('No. of events')
plt.bar(pos, N, width, color='r')
plt.show()








