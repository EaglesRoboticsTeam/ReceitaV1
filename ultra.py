import time
import brickpi3

BP = brickpi3.BrickPi3()
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)  
        
try:        #TENTANDO FECHAR O PROGRAMA                             
    while True:
        try:
            value = BP.get_sensor(BP.PORT_1) #TENTANDO CHAMAR O SENSOR ULTRASSONICO
            print(value) 
            if value >= 10: #SE O VALOR DO ULTRASSONICO FOR MAIOR OU IGUAL A 10
                BP.set_motor_power(BP.PORT_B + BP.PORT_C, 100) # O MOTOR VAI ANDAR PRA FRENTE 
                 
            else:  #E SE O O VALOR DO SENSOR UTRASSONICO FOR MENOR QUE 10
                BP.set_motor_power(BP.PORT_B + BP.PORT_C, 0) #O MOTOR VAI PARAR 
        except brickpi3.SensorError as error: #CASO O SENSOR DEMORE PARA INICIALIZAR O SENSOR ERRO SERVE PARA 
            print(error)
except KeyboardInterrupt: #FECHANDO O PROGRAMA
    BP.reset_all()
    
        
    
            
  
            