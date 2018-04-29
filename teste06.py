import time
import brickpi3

BP = brickpi3.BrickPi3()
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)
BP.set_sensor_type(BP.PORT_2, BP.SENSOR_TYPE.TOUCH)

try:        #TENTANDO FECHAR O PROGRAMA                             
    while True:
        try:
            value2 = BP.get_sensor(BP.PORT_2)#CHAMANDO O SENSOR DE TOQUE
            value = BP.get_sensor(BP.PORT_1) #TENTANDO CHAMAR O SENSOR ULTRASSONICO
            print(value) 
            if value >= 10: #SE O VALOR DO ULTRASSONICO FOR MAIOR OU IGUAL A 10
                BP.set_motor_power(BP.PORT_B + BP.PORT_C, 100) # O MOTOR VAI ANDAR PRA FRENTE 
                 
            elif value < 10:  #E SE O O VALOR DO SENSOR UTRASSONICO FOR MENOR QUE 10
                BP.set_motor_power(BP.PORT_B + BP.PORT_C, 50) #O motor reduz a velocidade em 50%
                if value2 == 1: #Caso o sensor de toque seja precionado
                    BP.set_motor_power(BP.PORT_B + BP.PORT_C, 0)
                    time.sleep(2)
                    BP.set_motor_power(BP.PORT_B + BP.PORT_C, -100)#os motores irão parar
                    time.sleep(1)
                    if value2 == 0:
                        BP.set_motor_power(BP.PORT_B, 0)
                        
        except brickpi3.SensorError as error: #CASO O SENSOR DEMORE PARA INICIALIZAR O SENSOR ERRO SERVE PARA 
            print(error)
except KeyboardInterrupt: #FECHANDO O PROGRAMA
    BP.reset_all()
  
        
    
            
  
            
