import time
import brickpi3

BP = brickpi3.BrickPi3()

def motor_on(speed, tempo, porta):
    try:
        BP.set_motor_power(porta,speed)       
        #Caso seja infinito usa '00'
        if tempo == '00':
            while True:  
                BP.set_motor_power(porta,speed)    
        else:                     
            time.sleep(tempo)
            BP.reset_all()
                   
    except KeyboardInterrupt:
                       BP.reset_all()
    
                       
motor_on(100, '00',BP.PORT_B)


            
    
    
     
    
