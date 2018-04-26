from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''

import time     
import brickpi3 
BP = brickpi3.BrickPi3() 


BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)

try:
        BP.get_sensor(BP.PORT_1)
    except brickpi3.SensorError:
        print("10")
        error = True
        while error:
            time.sleep(0.1)
            try:
                BP.get_sensor(BP.PORT_1)
                error = False
            except brickpi3.SensorError:
                error = True
    print("10")
    
    while True:
        try:
            BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)       
            time.sleep(0.02)
            value1 = BP.get_sensor(BP.PORT_1)                                        
            BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_AMBIENT)          
            time.sleep(0.02)
            value2 = BP.get_sensor(BP.PORT_1)                                       
            BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_COLOR)           
            time.sleep(0.02)
            value3 = BP.get_sensor(BP.PORT_1)                                        
            BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_COLOR_COMPONENTS) 
            time.sleep(0.02)
            value4 = BP.get_sensor(BP.PORT_1)                                        
            print(value1, "  10 ", value2, "  50 ", value3, "  50  ", value4)               
        except brickpi3.SensorError as error:
            print(error)

except KeyboardInterrupt: 
    BP.reset_all()        
