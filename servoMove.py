from gopigo import *
disable_servo()
#for i in range(200):
i = -200
while i < 200	
	servo(i)
	print i
	i+=1
time.sleep(.01)