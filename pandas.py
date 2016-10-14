import math
import numpy as np

file=open('pandas.txt','r')

sum=0.0
i=0
z=[]						#defined a list z 

while i<1000:

	num=file.readline()		#num stores a line from input file(pandas.txt) one by one as string
	sum= (sum)+float(num)   #float(num) converts string in number and sum adds number one by one as loop runs
	z.append(float(num))    #input weight of babies get store in array z
	i=i+1


print ('sum of weight of all babies=',np.around(sum,decimals=2))	#print sum of weights of all babies round off to decimals 2


mean =np.mean(z)								#gives mean of weight of babies
mean_error=(np.std(z))/(math.sqrt(999))

print ('mean=',np.around(mean,decimals=2))
print ('mean error=',np.around(mean_error,decimals=2))


fluc=mean_error*(math.sqrt(1000))

print ('Typical fluctuations in weight of each baby about its mean =',np.around(fluc,decimals=2))

file.close()