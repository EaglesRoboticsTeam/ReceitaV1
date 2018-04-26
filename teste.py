from brickpi3 import *

BrickPi3Setup()
BrickPi3.MotorEnable[PORT_A] = 1
BrickPi3SetupSensors()
BrickPi3.MotorSpeed[PORT_A] = 200
BrickPi3UpdateValues()
        
run_motors()    

