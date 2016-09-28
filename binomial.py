import matplotlib.pyplot as plt
import numpy as np
import math

def factorial(n): 	 # defined a function factorial to calculate factorial of a number n
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)



y=[]			# defined an array to store the values of binomial distribution function for variable k

p=0.4			# set probability of favourable outcome 0.4

n=50			# total no of events 50


def binomial(k):        #defined binomial pdf here

	return ((factorial(n)*(p**k)*((1-p)**(n-k)))/(factorial(k)*factorial(n-k)))



x= np.linspace(0, 49, 50)  #linspace function provides 50 integer values of pdf variable(x) ranging from 0 to 49

i=0
while i<50:
	y.append(binomial(i))   #values of pdf stores in array as loop runs
	i=i+1
	
plt.plot(x,y,'ro')
plt.xlabel('k')
plt.ylabel('Binomial distribution fuction,B(k)')
plt.title('Binomial distribution Plot')
plt.text(40, 0.11, r'p=0.4')
plt.text(40, 0.10, r'n=50')

plt.show()
