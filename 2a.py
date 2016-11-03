
import numpy as np
import matplotlib.pyplot as plt
import math

file=open('recoilenergydata_EP219.csv','r')

x=[]
y=[]
N= []

num_bins=40
i=0
while i<40:

	[Er, Events]=file.readline().split(',')
	x.append(float(Er))
	y.append(float(Events)) 	
	i=i+1

plt.figure()
plt.title('Histogram of actual data')
plt.xlabel('Measured recoil energies(Kev)')
plt.ylabel('No. of events')


width = 1.0     # gives histogram aspect to the bar diagram


pos = np.arange(len(x))
plt.bar(pos, y, width, color='r')
plt.show()








