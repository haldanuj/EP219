import random
import matplotlib.pyplot as plt
import numpy as np
import math

def genNum():	        # defined a function genNum which generates single random no between 0 &1
	num=random.random()
	return num

z=[] 		       #defined an array which stores the values of pi
j=0		       #while loop begins
while j<500:
	i=0
	cirIn=0
	recIn=0
	while i<2000:
		x=2*genNum()       # x(random no.) lies in range of [0,2)
		y=2*genNum()	   # y(random no.) lies in range of [0,2)
		if math.sqrt((x-1)*(x-1)+(y-1)*(y-1))<=1:
			cirIn = cirIn+1
		else:
			recIn=recIn + 1
		i = i+1
	ratio =cirIn/(recIn+cirIn)
	pi=4*ratio
	
	z.append(pi)    # one value of pi is added to z array as loop runs at a time
	j=j+1

plt.hist(z)
plt.show()
