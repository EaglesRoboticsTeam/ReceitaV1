#versão 0.2.5
import time
import brickpi3

BP = brickpi3.BrickPi3()

BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_COLOR)

color = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

try:
    while True:
        try:
            value = BP.get_sensor(BP.PORT_1)#value recebe valores do sensor da porta 1
            
            if color[value] == "Black":
                time.sleep(0.001)
                print("Motor A 100")
                
            else:
                time.sleep(0.001)
                print("Motor B 100")
                
        except brickpi3.SensorError as error: #CASO O SENSOR DEMORE PARA INICIALIZAR O SENSOR ERRO SERVE PARA 
            print(error)
except KeyboardInterrupt: #FECHANDO O PROGRAMA
    BP.reset_all()


