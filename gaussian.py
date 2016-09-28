import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

mean =0
variance = 1

sigma = math.sqrt(variance)

x = np.linspace(-10, 10, 100)			#sets x coordinate of the plot from -10 to 10 taking 100 values of variable(x)


plt.plot(x,mlab.normpdf(x, mean, sigma))	#draws gaussian distribution 

plt.xlabel('x')

plt.ylabel('Gaussian distribution fuction')	

plt.title('Gaussian distribution graph')	#used this command to give title to plot

plt.text(5, 0.35, r'mean =0')                   #prints "mean =0" on the plot

plt.text(5, 0.33, r'variance =1')		#prints "variance=1" on the plot 

plt.show()
