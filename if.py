from __future__ import print_function
from __future__ import division
import time
import brickpi3

BP = brickpi3.BrickPi3()

def motor_A(velocidadeA, tempoA):

    try:
        value = 1
        while not value:
            try:
                value = 1
            except brickpi3.SensorError:
                pass
        
        speed = velocidadeA
        adder = 1
        BP.set_motor_power(BP.PORT_A,speed)
        
        #Caso seja infinito usa '00'
        if tempoA == '00':
            while True:
  
                value = 1
                while not value:
                    try:
                        value = 1
                    except brickpi3.SensorError:
                        pass
        
                speed = velocidadeA
                adder = 1
                BP.set_motor_power(BP.PORT_A,speed)    
        else:                     
            time.sleep(tempoA)
            BP.reset_all()
                   
    except KeyboardInterrupt:
                       BP.reset_all()
                       
def motor_B(velocidadeB, tempoB):

    try:
        value = 1
        while not value:
            try:
                value = 1
            except brickpi3.SensorError:
                pass
        
        speed = velocidadeB
        adder = 1
        BP.set_motor_power(BP.PORT_B,speed)
        
        #Caso seja infinito usa '00'
        if tempoB == '00':
            while True:
  
                value = 1
                while not value:
                    try:
                        value = 1
                    except brickpi3.SensorError:
                        pass
        
                speed = velocidadeB
                adder = 1
                BP.set_motor_power(BP.PORT_B,speed)    
        else:                     
            time.sleep(tempoB)
            BP.reset_all()
                   
    except KeyboardInterrupt:
                       BP.reset_all()
                       
def motor_C(velocidadeC, tempoC):

    try:
        value = 1
        while not value:
            try:
                value = 1
            except brickpi3.SensorError:
                pass
        
        speed = velocidadeC
        adder = 1
        BP.set_motor_power(BP.PORT_C,speed)
        
        #Caso seja infinito usa '00'
        if tempoC == '00':
            while True:
  
                value = 1
                while not value:
                    try:
                        value = 1
                    except brickpi3.SensorError:
                        pass
        
                speed = velocidadeC
                adder = 1
                BP.set_motor_power(BP.PORT_C,speed)    
        else:                     
            time.sleep(tempoC)
            BP.reset_all()
                   
    except KeyboardInterrupt:
                       BP.reset_all()
                       
def motor_D(velocidadeD, tempoD):

    try:
        value = 1
        while not value:
            try:
                value = 1
            except brickpi3.SensorError:
                pass
        
        speed = velocidadeD
        adder = 1
        BP.set_motor_power(BP.PORT_D,speed)
        
        #Caso seja infinito usa '00'
        if tempoD == '00':
            while True:
  
                value = 1
                while not value:
                    try:
                        value = 1
                    except brickpi3.SensorError:
                        pass
        
                speed = velocidadeD
                adder = 1
                BP.set_motor_power(BP.PORT_D,speed)    
        else:                     
            time.sleep(tempoD)
            BP.reset_all()
                   
    except KeyboardInterrupt:
                       BP.reset_all()
                       
def motor_on(motor1, motor2):
    if motor1 == 'motor_A' or motor2 == 'motor_A':
        motor_A(velocidadeA, tempoA)
    elif mmotor_B(velocidadeB, tempoB)
    motor_C(velocidadeC, tempoC)
    motor_D(velocidadeD, tempoD)
    motor_B + motor_C

motor_on(100, 2 + -100, 2)
    
    

            
    
    
     
    

