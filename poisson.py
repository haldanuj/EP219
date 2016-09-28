import matplotlib.pyplot as plt
import numpy as np
import math


def factorial(n):               # defined a function factorial to calculate factorial of a number
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

L=5				#provided any arbitrary value to mean(L) of pdf

y=[]				# defined an array to store the values of poisson distribution function for variable x

def poisson(x):			#defined pdf here
	M=L**x
	return (np.exp(-L)*(L**x)/factorial(x))
	
x = np.linspace(0, 49, 50)	#linspace function provides 50 integer values of pdf variable(x) ranging from 0 to 49

i=0				#initialised i
while i<50:
    y.append(poisson(i))	 #values of pdf stores in arry as loop runs
    i=i+1
    
plt.plot(x,y, 'ro')
plt.xlabel('x')
plt.ylabel('Poisson distribution fuction,p(x)')
plt.title('Poisson distribution Plot')
plt.text(40, 0.15, r'mean = 5')


plt.show()