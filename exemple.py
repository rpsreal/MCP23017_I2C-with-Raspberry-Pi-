#!/usr/bin/python
'''
Exemple 'How to use the library MCP23017_I2C' - Rui Pedro Silva; Portugal; 03/2015
Connect a switch to GPB7 and led to GPA0. This program will make the LED turn on when you turn the switch.
'''
from MCP23017_I2C import *

GPIO_CHIP_1 = GPIO_CHIP(0x20, 1) # define chip MCP23017_I2C
#   GPIO_CHIP( Device address, Pi Model )
# 0 = Model A, B Rev 2 or B+ Pi ; 1 = Model B Rev 1 Pi) 

GPIO_CHIP_1.setup( 0, 'OUT', 'A') # configure GPA0 like output
GPIO_CHIP_1.setup( 7, 'IN', 'B') # configure GPB7 like input
# GPIO_CHIP.setup(pin, io, side)
# 	pin (0 - 7)  io (IN or OUT)  side (A or B)


# You can use another MCP23017, write:
#GPIO_CHIP_2 = GPIO_CHIP(0x21, 1) # define another chip MCP23017_I2C

#GPIO_CHIP_2.setup( 0, 'OUT', 'A') # configure GPA0 like output
#GPIO_CHIP_2.setup( 7, 'IN', 'B') # configure GPB7 like input

try:
	while 1:
		switch = GPIO_CHIP_1.input(7, 'B') # save the state of GPB7 in 'switch'
		# GPIO_CHIP.input(pin, side)
		# 	pin (0 - 7)  side (A or B)
		
		if switch==1:
			print 'Led ON'
			GPIO_CHIP_1.output(0, 1, 'A') # write in GPA0 1 (high)
		else:
			print 'Led OFF'
			GPIO_CHIP_1.output(0, 0, 'A') # write in GPA0 0 (LOW)
			# GPIO_CHIP.output(pin, hl, side)
			# 	pin (0 - 7)  hl (0 or 1)  side (A or B)

		# With one second chip:
		#switch2 = GPIO_CHIP_2.input(7, 'B')
		#if switch2==1:
		#	print 'Led2 ON'
		#	GPIO_CHIP_2.output(0, 1, 'A') # write in GPA0 1 (high)
		#else:
		#	print 'Led2 OFF'
		#	GPIO_CHIP_2.output(0, 0, 'A') # write in GPA0 0 (LOW)
		
except KeyboardInterrupt:
	print 'End exemple.py!'
