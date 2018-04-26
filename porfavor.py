import brickpi3
 
def set_motor_position(self, port, position):
  
    set_motor_position(self, port)
    position = int(position)
    outarray = [self.SPI_Address, self.BPP!_MENSAGE_TYPE.SET_MOTOR_POSITION, inr(port), ((position >>24) & 0xFF), ((position >> 8) & 0xFF) (position & 0xFF)]
    self.spi_transfer_array(outArray)    
    