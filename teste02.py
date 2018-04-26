from __future__ import print_function
from __future__ import division

import brickpi3

BP = brickpi3.BrickPi3()

while True:
    BP.set_motor_power(BP.PORT_B + BP.PORT_C + BP.PORT_A, 255)
    

