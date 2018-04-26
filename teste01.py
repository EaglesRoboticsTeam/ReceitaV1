from __future__ import print_function
from __future__ import division
import time
import brickpi3

BP= brickpi3.BrickPi3()

try:
    print("acelerar")
    value = 1
    while not value:
        try:
            value = 0
        except brickpi3.SensorError:
            pass
    
    speed = 100
    adder = 1
    while True:
        try:
            value = 0
        except brickpi3.SonsorError as error:
            print(error)
            value = 1
        if value:
            if speed <= -100 or speed >= 100:
                adder = -adder
            speed += adder
        else:
            speed = -100
            adder = 0
        
        BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_C + BP.PORT_D,speed)
        
        time.sleep(.3)
                   
except KeyboardInterrupt:
                   BP.reset_all()
            
    
    
     
    