import time
import brickpi3

BP = brickpi3.BrickPi3()

BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_COLOR_COLOR)

color = ["none", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

try:
    while True:
        try:
            value = BP.get_sensor(BP.PORT_1)#value recebe valores do sensor da porta 1
            print(color[value])
            
            if value == "Black":
                BP.set_motor_power(BP.PORT_A, 100)
                if value == "White":
                    BP.set_motor_power(BP.PORT_B, 100)
                else:
                    pass
            else:
                pass
            
        except brickpi3.SensorError as error: #CASO O SENSOR DEMORE PARA INICIALIZAR O SENSOR ERRO SERVE PARA 
            print(error)
except KeyboardInterrupt: #FECHANDO O PROGRAMA
    BP.reset_all()
