
import time
import brickpi3

BP = brickpi3.BrickPi3()

def motor(porta, speed):
    BP.set_motor_power(porta, speed)

except KeyboardInterrupt:
                       BP.reset_all()

        
motor(BP.PORT_C, 100)
