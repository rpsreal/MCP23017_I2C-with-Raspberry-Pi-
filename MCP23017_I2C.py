#!/usr/bin/python
import smbus # To install this -> sudo apt-get install -y python-smbus i2c-tools

# ------- config the chip MCP23017 I2C Port Expander --------
#from MCP23017_I2C import *
#port_expander=[0x20, 0x00,0x00,0x00,0x00, 1] 
# Device address, -R-, -R-, -R-, -R-, (0->Model A, B Rev 2 or B+ Pi ;1->Model B Rev 1 Pi) 


def GPIO_CHIP_SETUP( pin, io, side, port_expander):
# GPIO_CHIP_SETUP( 0, 'OUT', 'A', port_expander)
# pin (0,7)  io (IN,OUT)  side (A,B)
	try:
		bus = smbus.SMBus(port_expander[5])
		IODIRB = 0x01 # Pin direction register
		IODIRA = 0x00 # Pin direction register
		DEVICE = port_expander[0] 
		
		act_ioA = port_expander[1]
		act_ioB = port_expander[2]
		if (pin<0 or pin>7) or (side!='A' and side!='B') or (io!='IN' and io!='OUT'):
			print ' --- GPIO_CHIP_SETUP(pin, io, side, port_expander) ---'
			print ' --- pin (0 - 7)  io (IN or OUT)  side (A or B) ---'
			return;
		else:
	
			if io=='IN' and side=='A':
				pinio  = act_ioA | (1<<pin)
				act_ioA=pinio
			else:
				if io=='OUT' and side=='A':
					pinio  = act_ioA & ~(1<<pin)
					act_ioA=pinio
				else:
					if io=='IN' and side=='B':
						pinio  = act_ioB | (1<<pin)
						act_ioB=pinio
					else:
						if io=='OUT' and side=='B':
							pinio  = act_ioB & ~(1<<pin)
							act_ioB=pinio
	    
			if side=='A':
				bus.write_byte_data(DEVICE,IODIRA,pinio)
			else:
				bus.write_byte_data(DEVICE,IODIRB,pinio)

		port_expander[1] = act_ioA
		port_expander[2] = act_ioB
		return port_expander;

	except:
		print ' --- Error accessing the chip MCP23017 ---'
		raise
    
    
    
def GPIO_CHIP_WRITE( pin, hl, side, port_expander):
# GPIO_CHIP_WRITE(0, 1, 'A', port_expander) 
# pin (0,7)  hl (0,1)  side (A,B)
	try:
		bus = smbus.SMBus(port_expander[5])  
		OLATA = 0x14 # Register for outputs
		OLATB = 0x15 # Register for outputs
		DEVICE = port_expander[0] 
    
		act_pinA = port_expander[3]
		act_pinB = port_expander[4]
    
		if (pin<0 or pin>7) or (side!='A' and side!='B') or (hl!=1 and hl!=0):
			print ' --- GPIO_CHIP_WRITE(pin, hl, side, port_expander) ---'
			print ' --- pin (0 - 7)  hl (0 or 1)  side (A or B) ---'
			return;
		else:
			if hl==1 and side=='A':
				pinhl  = act_pinA | (1<<pin)
				act_pinA=pinhl
			else:
				if hl==0 and side=='A':
					pinhl  = act_pinA & ~(1<<pin)
					act_pinA=pinhl
				else:
					if hl==1  and side=='B':
						pinhl  = act_pinB | (1<<pin)
						act_pinB=pinhl
					else:
						if hl==0 and side=='B':
							pinhl  = act_pinB & ~(1<<pin)
							act_pinB=pinhl
			if side=='A':
				bus.write_byte_data(DEVICE,OLATA,pinhl)
			else:
				bus.write_byte_data(DEVICE,OLATB,pinhl)
  
		port_expander[3] = act_pinA
		port_expander[4]= act_pinB
		return port_expander;
    
	except:
		print ' --- Error accessing the chip MCP23017 ---'
		raise


def GPIO_CHIP_READ( pin, side, port_expander):
# Teste = GPIO_CHIP_READ(7, 'B', port_expander)
# pin (0,7)  side (A,B)
	try:
		bus = smbus.SMBus(port_expander[5]) 	
		GPIOA = 0x12 # Register for inputs
		GPIOB = 0x13 # Register for inputs
		DEVICE = port_expander[0] 
  	
		if (pin<0 or pin>7) or (side!='A' and side!='B'):
			print ' --- MySwitch = GPIO_CHIP_READ(pin, side, port_expander) ---'
			print ' --- pin (0 - 7)  side (A or B) ---'
			return;
		else:
			if side=='A':
				MySwitch = bus.read_byte_data(DEVICE,GPIOA)
				if MySwitch & (1<<pin) == (1<<pin):
					MySwitch=1
				else:
					MySwitch=0
			else:
				MySwitch = bus.read_byte_data(DEVICE,GPIOB)
				if MySwitch & (1<<pin) == (1<<pin):
					MySwitch=1
				else:
					MySwitch=0
  
		return MySwitch;
	except:
		print ' --- Error accessing the chip MCP23017 ---'
		raise


