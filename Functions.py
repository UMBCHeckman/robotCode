from __future__ import print_function
from __future__ import division

import time

import gopigo3

GPG = gopigo3.GoPiGo3()


#function written referencing code from https://github.com/DexterInd/GoPiGo3/blob/master/Software/Python/Examples/Motor.py
def driveLeft(forOrBack):
    i = 0
    while True:
        GPG.set_motor_power(GPG.MOTOR_LEFT, i * forOrBack)
        i+= 1
        time.sleep(0.02)

#function written referencing code from https://github.com/DexterInd/GoPiGo3/blob/master/Software/Python/Examples/Motor.py
def driveRight(forOrBack):
    i = 0
    while True:
        GPG.set_motor_power(GPG.MOTOR_LEFT, i * forOrBack)
        i+= 1
        time.sleep(0.02)

#function written referencing code from https://github.com/DexterInd/GoPiGo3/blob/master/Software/Python/Examples/Motor.py
def driveForward():
    i = 0
    while True:
        GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, i)
        i+= 1
        time.sleep(0.02)

#function written referencing code from https://github.com/DexterInd/GoPiGo3/blob/master/Software/Python/Examples/Motor.py
def driveBackward():
    i = 0
    while True:
        GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, -i)
        i+= 1
        time.sleep(0.02)

#following encoder functions written referencing code from https://github.com/DexterInd/GoPiGo3/blob/master/Software/Python/easygopigo3.py
def wheelEncoderLeft():
    print(GPG.get_motor_encoder(GPG.MOTOR_LEFT))

def wheelEncoderRight():
    print(GPG.get_motor_encoder(GPG.MOTOR_RIGHT))

def wheelEncoderLeftCont():
    while True:
        print(GPG.get_motor_encoder(GPG.MOTOR_LEFT))

def wheelEncoderRightCont():
    while True:
        print(GPG.get_motor_encoder(GPG.MOTOR_RIGHT))

def rightDeg(numDegrees):
    for i in range(0,90):
        driveRight(1)
    
try:
    while True:
        for i in range(-100,51):
            GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, -i)
            #wheelEncoder()
            time.sleep(0.02)

        for i in range(-50, 101):
            GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, i)
            time.sleep(0.02)
except KeyboardInterrupt:
    GPG.reset_all()
