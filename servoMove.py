from gopigo import *
disable_servo()
for i in range(200):
	
	servo(i)
	print i
time.sleep(.01)