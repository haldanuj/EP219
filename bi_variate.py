
import numpy as np
import matplotlib.pyplot as plt
import math


#code begins for drawing contours of 2d Gaussian pdf
delta = 0.25
x = np.arange(-8, 8, delta)
y = np.arange(-8, 8, delta)
X, Y = np.meshgrid(x, y)


s1=3
s2=math.sqrt(6)
mu1=0
mu2=0
ro=(-2/(s1*s2))


'''
Below defined Gaussian pdf in 2 variables having mean1(mu1)=0,mean2(mu2)=0
standard deviation1(s1)=3 , standard deviation2=sqrt(6) and covariance =-2
'''


def BiGaussian(s1,s2,mu1,mu2,ro):
	Sq= math.sqrt(1-(ro*ro))
	Z3=(((X-mu1)/s1)*((X-mu1)/s1)) + (((Y-mu2)/s2)*((Y-mu2)/s2)) - ((2*ro*(X-mu1)*(Y-mu2))/(s1*s2))

	Z1= (1/(2*3.14*s1*s2*Sq))
	Z2=np.exp(-Z3/(2*Sq*Sq))

	Z=Z1*Z2

	return Z


plt.figure()
CS = plt.contour(X, Y, BiGaussian(s1,s2,mu1,mu2,ro))

plt.title('Gaussian pdf\'s contours')
plt.axvline(0, color='b', linestyle='dashed', linewidth=2)
plt.axhline(0, color='b', linestyle='dashed', linewidth=2)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.text(4, 7, r'sigma(x)=3')
plt.text(4,6, r'sigma(y)=sqrt(6)')
plt.text(4, 5, r'sigma(xy)=-2')
plt.show()
# code ends for drawing contours of 2d Gaussian pdf




#code begins for drawing 2d histogram from random generated pairs satisfying 2d Gaussian pdf
mean =(0,0)
cov=[[9,-2],[-2,6]]

a1=[]
a2=[]
z=[]
sum=0 
j=0
while j<1000:

	xx, yy = np.random.multivariate_normal(mean, cov)   #xx,yy tuple is random generated pair satisfying 2d Gaussian pdf 
	s1 =str(xx)											#converting tuple to string
	s2=str(yy)
	z1=((6*float(s1)*float(s1)) + (4*float(s1)*float(s2)) + (9*float(s2)*float(s2)))/50
	sum=sum+z1
	
	z.append(z1)
	a1.append(xx)
	a2.append(yy)
   
	j=j+1

xx, yy = np.random.multivariate_normal(mean, cov, 100000).T

#A1 and A2 are arrays to store random generated pairs satisfying 2d Gaussian pdf 
A1=np.array(a1)
A2=np.array(a2)


plt.figure()
plt.hist2d(xx,yy, 150)
plt.colorbar()
plt.title('2D Gaussian histogram')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.text(5,9, r'sigma(x)=3',bbox={'facecolor':'red'})
plt.text(5,8, r'sigma(y)=sqrt(6)',bbox={'facecolor':'red'})
plt.text(5,7, r'sigma(xy)=-2',bbox={'facecolor':'red'})
plt.show()
#code ends for drawing 2d histogram from random generated pairs satisfying 2d Gaussian pdf

	
#code for generating and ploting histogram for z=(6*x*x + 4*y*x + 9*y*y)/50 where x, y are random generated pairs generated above 
#variable sum have sum of all  z=(6*x*x + 4*y*x + 9*y*y)/50 where x, y are random generated pairs generated above 
mean= sum/1000
print ('mean=',np.around(mean,decimals=2))
print ('std deviation=',np.around(np.std(z),decimals=2))


plt.figure()
plt.title('1 D histogram of z=(6*x*x + 4*y*x + 9*y*y)/50')
plt.xlabel('Bins')
plt.ylabel('Frequency')

plt.hist(z)
plt.show()
