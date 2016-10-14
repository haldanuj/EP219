import matplotlib.pyplot as plt
import numpy as np
import math

file=open('linearexpansion.txt','r')
#code begins for drawing scatter plot of rod's length varying with temperature
#defined 2 lists x and y to store temperature and rod's length repectively 

x= []
y =[]
i=0
while i<50:

	[num, temp]=file.readline().split(',')
	x.append(float(num))  				
	y.append(float(temp))
	#print (float(num),temp)
	i=i+1

xx = np.array(x)
yy = np.array(y)

plt.title('Scatter plot of Aluminium rod')
plt.xlabel('Temperature(Degrees C)')
plt.ylabel('Length(In mm)')
plt.plot(xx, yy, 'bo', markersize=4)
plt.show()
#code ends for drawing scatter plot of rod's length varying with temperature



j=0
sum_x=0					 #sum_x stores the sum of all values of temperature
sum_y=0					#sum_y stores the sum of all values of rod's lengths
while j<50:
	sum_x=sum_x + x[j]
	sum_y=sum_y + y[j]
	j=j+1

mean_x=(sum_x)/50  		#mean_x gives mean of temperature
mean_y=(sum_y)/50       #mean_y gives mean of rod's length                         

cross_sum=0             #cross_sum gives sum of (x(k)-mean_x)*(y(k)-mean_y) varying k from 0 to n-1
sum_xx=0				# sum_xx gives sum of (x(k)-mean_x)*(x(k)-mean_x) varying k from 0 to n-1
sum_xx=0
k=0
while k<50:
	
	cross_sum=cross_sum +((x[k]-mean_x)*(y[k]-mean_y))
	sum_xx=sum_xx + ((x[k]-mean_x)*(x[k]-mean_x))
	
	k=k+1

best_slope= (cross_sum)/sum_xx
best_intercept=mean_y-(best_slope*mean_x)

print ('Best Intercept=',np.around(best_intercept,decimals=2))
print ('Best Slope=',np.around(best_slope,decimals=3))


# Created a list of values of y(rod's length) in the best fit line
abline_values=[]
n=0
while n<50:

	abline_values.append(best_slope *x[n] + best_intercept)
	n=n+1


# Plot the best fit line over the actual values
plt.plot(x, y, 'bo')
plt.plot(x, abline_values, 'b')
plt.title('Scatter plot with best fit line')
plt.xlabel('Temperature(Degree C)')
plt.ylabel('Rod\'s length (In mm)')
plt.text(0.2,1225,'Best fit Y Intercept= 993.51mm')
plt.text(0.2,1250,'Best fit Slope =22.902')
plt.show()


print ('Best estimate for Length of the rod at 0 degrees celsius =',np.around(best_intercept,decimals=2))


y2=(best_slope*x[2]) + (best_intercept)
y1=(best_slope*x[1]) + (best_intercept)

linear_coeff=(y2-y1)/(y1*(x[2]-x[1]))
print ('coefficinet for linear expansion =',np.around(linear_coeff,decimals=3),'(1/Kelvin)')

length_15=(best_slope*15.)+ (best_intercept)
print ('expected length of the rod by extrapolation =',np.around(length_15,decimals=2))



#code for calculating error in extrapolation of bestfit line is following
Sq_sum=0
m=0
while m<49:
	Sq_sum=Sq_sum + ((y[m]-abline_values[m])*(y[m]-abline_values[m]))
	m=m+1

Error= math.sqrt(Sq_sum/48)
print ('error in calculating rod\'s length at 15 degrees celcius =',np.around(Error,decimals=2))

file.close()
