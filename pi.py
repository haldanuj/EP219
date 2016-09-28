import random
import math


def genNum():        		 # defined a function genNum which generates single random no between 0 &1
	num=random.random()
	return num


cirIn=0				# defined variable circleIn to store the random no's generated in circle of radius 1 centred at (1,1)

recIn=0				# defined variable recIn to store the random no's generated out of  circle of radius 1 centred at (1,1) but inside square of side=2 centred at (1,1)


i=0				# initialised variable i


while i<2000:			# while loop begins
	x=2*genNum()		# x(random no.) lies in range of [0,2)
	y=2*genNum()		# y(random no.) lies in range of [0,2)

	if math.sqrt((x-1)*(x-1)+(y-1)*(y-1))<=1:	# if random generated point(x,y) lies within circle then 1 more value gets added to cirIn
		cirIn = cirIn+1
	else:
		recIn=recIn + 1				# else random generated point(x,y) lies outside circle but inside rectangle then 1 more value gets added to recInIn
	i = i+1


ratio =cirIn/(recIn+cirIn)     # "ratio" is the ratio of total no of random generated points in cicle to total no of radom generated points in rectangle which is equivalent to ratio of their respective areas
pi=4*ratio


print (pi)      	#finally prints the value of pi
