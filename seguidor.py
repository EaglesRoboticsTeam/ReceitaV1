from __future__ import print_function 
from __future__ import division       

import time     
import brickpi3 

BP = brickpi3.BrickPi3() 

def motor_on(velocidade, tempo, porta):
    try:
        speed = velocidade
        BP.set_motor_power(porta, speed)

        if tempo == '00' :
            while True:
                speed = velocidade
                BP.set_motor_power(porta, speed)
       
            

BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)

try:
        BP.get_sensor(BP.PORT_1)
    except brickpi3.SensorError:
        print("Configuring...")
        error = True
        while error:
            time.sleep(0.1)
            try:
                BP.get_sensor(BP.PORT_1)
                error = False
            except brickpi3.SensorError:
                error = True
    print("Configured.")
    
    while True:
        try:
            BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)       
            motor_on(100, 3, BP.PORT_A)
            value1 = BP.get_sensor(BP.PORT_1)                                        
            BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_AMBIENT)
            motor_on(100, 3, BP.PORT_A)
            value2 = BP.get_sensor(BP.PORT_1)                                       
            BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_COLOR)           
            motor_on(100, 3, BP.PORT_A)
            value3 = BP.get_sensor(BP.PORT_1)                                        
            BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_COLOR_COMPONENTS) 
            motor_on(100, 3, BP.PORT_A)
            value4 = BP.get_sensor(BP.PORT_1)                                        
            print(value1, "  50 ", value2, " 10  ", value3, " 50  ", value4)               
        except brickpi3.SensorError as error:
            print(error)
            

except KeyboardInterrupt: 
    BP.reset_all()        
