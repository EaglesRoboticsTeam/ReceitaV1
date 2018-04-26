import time
import brickpi3

speedC = 50
speedB = -50
portaB = BP.PORT_B
portaC = BP.PORT_C

while True:
    BP.set_motor_power(portaB, speedB)
    BP.set_motor_power(portaC, speedC)
    
except KeyboardInterrupt:
                       BP.reset_all()
                       
