### Exemple 'How to use the library MCP23017_I2C' - Rui Pedro Silva; Portugal; 03/2015
### Connect a switch to GPB7 and led to GPA0. This program will make the LED turn on when you turn the switch.

from MCP23017_I2C import *
port_expander=[0x20, 0x00,0x00,0x00,0x00, 1] 
#   Device address, -R-, -R-, -R-, -R-, Pi Model
# 0 = Model A, B Rev 2 or B+ Pi ; 1 = Model B Rev 1 Pi) 


port_expander = GPIO_CHIP_SETUP( 0, 'OUT', 'A', port_expander) # configure GPA0 like output
port_expander = GPIO_CHIP_SETUP( 7, 'IN', 'B', port_expander) # configure GPB7 like input
# port_expander = GPIO_CHIP_SETUP(pin, io, side, port_expander)
# 	pin (0 - 7)  io (IN or OUT)  side (A or B)

while 1:
	switch = GPIO_CHIP_READ(7, 'B', port_expander) # save the state of GPB7 in 'switch'
	# GPIO_CHIP_READ(pin, side, port_expander)
	# pin (0 - 7)  side (A or B)

	if switch==1:
		print 'Led ON'
		port_expander = GPIO_CHIP_WRITE(0, 1, 'A', port_expander) # write in GPA0 1 (high)
	else:
		print 'Led OFF'
		port_expander = GPIO_CHIP_WRITE(0, 0, 'A', port_expander) # write in GPA0 0 (LOW)
		# port_expander = GPIO_CHIP_WRITE(pin, hl, side, port_expander)
		# 	pin (0 - 7)  hl (0 or 1)  side (A or B)
