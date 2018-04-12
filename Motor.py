from __future__ import print_function
from __future__ import division

import time

import gopigo3

GPG = gopigo3.GoPiGo3()



def driveLeft(forOrBack):
    i = 0
    while True:
        GPG.set_motor_power(GPG.MOTOR_LEFT, i * forOrBack)
        i+= 1
        time.sleep(0.02)
        
def driveRight(forOrBack):
    i = 0
    while True:
        GPG.set_motor_power(GPG.MOTOR_LEFT, i * forOrBack)
        i+= 1
        time.sleep(0.02)
        
def driveForward():
    i = 0
    while True:
        GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, i)
        i+= 1
        time.sleep(0.02)
try:
    while True:
        for i in range(-100,51):
            GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, -i)
            time.sleep(0.02)

        for i in range(-50, 101):
            GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, i)
            time.sleep(0.02)
except KeyboardInterrupt:
    GPG.reset_all()
