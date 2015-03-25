#!/usr/bin/python
'''
 - MCP23017_I2C - 
Library Python for Raspberry Pi
Developed by Rui Pedro Silva; Portugal; 03/2015
'''
import smbus # To install this -> sudo apt-get install -y python-smbus i2c-tools

# ------- config the chip MCP23017 I2C Port Expander --------
#from MCP23017_I2C import *
#	GPIO_CHIP = GPIO_CHIP(0x20, 1)
#	 	    GPIO_CHIP( Device address, Pi Model )
# 0 = Model A, B Rev 2 or B+ Pi ; 1 = Model B Rev 1 Pi) 


class GPIO_CHIP:
	def __init__(self, device_address, pi_model): 
			self.device_address = device_address #DEVICE
			self.pi_model = pi_model
			self.bus = smbus.SMBus(pi_model)
			
			self.act_ioA = 0x00
			self.act_ioB = 0x00
			self.act_pinA = 0x00
			self.act_pinB = 0x00

			self.IODIRB = 0x01 # Pin direction register
			self.IODIRA = 0x00 # Pin direction register
			self.OLATA = 0x14 # Register for outputs
			self.OLATB = 0x15 # Register for outputs
			self.GPIOA = 0x12 # Register for inputs
			self.GPIOB = 0x13 # Register for inputs


	def setup(self, pin, io, side):
	# GPIO_CHIP.setup( 0, 'OUT', 'A')
	# pin (0,7)  io (IN,OUT)  side (A,B)
		try:

			if (pin<0 or pin>7) or (side!='A' and side!='B') or (io!='IN' and io!='OUT'):
				print ' --- GPIO.setup(pin, io, side) ---'
				print ' --- pin (0 - 7)  io (IN or OUT)  side (A or B) ---'
				return;
			else:
	
				if io=='IN' and side=='A':
					pinio  = self.act_ioA | (1<<pin)
					self.act_ioA=pinio
				else:
					if io=='OUT' and side=='A':
						pinio  = self.act_ioA & ~(1<<pin)
						self.act_ioA=pinio
					else:
						if io=='IN' and side=='B':
							pinio  = self.act_ioB | (1<<pin)
							self.act_ioB=pinio
						else:
							if io=='OUT' and side=='B':
								pinio  = self.act_ioB & ~(1<<pin)
								self.act_ioB=pinio
		    
				if side=='A':
					self.bus.write_byte_data(self.device_address,self.IODIRA,pinio)
				else:
					self.bus.write_byte_data(self.device_address,self.IODIRB,pinio)
	
			return;

		except:
			print ' --- Error accessing the chip MCP23017 ---'
			raise
    
    
    
	def output(self, pin, hl, side):
	# GPIO_CHIP.output(0, 1, 'A') 
	# pin (0,7)  hl (0,1)  side (A,B)
		try:
	
			if (pin<0 or pin>7) or (side!='A' and side!='B') or (hl!=1 and hl!=0):
				print ' --- GPIO.output(pin, hl, side) ---'
				print ' --- pin (0 - 7)  hl (0 or 1)  side (A or B) ---'
				return;
			else:
				if hl==1 and side=='A':
					pinhl  = self.act_pinA | (1<<pin)
					self.act_pinA=pinhl
				else:
					if hl==0 and side=='A':
						pinhl  = self.act_pinA & ~(1<<pin)
						self.act_pinA=pinhl
					else:
						if hl==1  and side=='B':
							pinhl  = self.act_pinB | (1<<pin)
							self.act_pinB=pinhl
						else:
							if hl==0 and side=='B':
								pinhl  = self.act_pinB & ~(1<<pin)
								self.act_pinB=pinhl
				if side=='A':
					self.bus.write_byte_data(self.device_address,self.OLATA,pinhl)
				else:
					self.bus.write_byte_data(self.device_address,self.OLATB,pinhl)
	
			return;
	    
		except:
			print ' --- Error accessing the chip MCP23017 ---'
			raise
	
	
	def input(self, pin, side):
	# Teste = GPIO_CHIP.input(7, 'B', port_expander)
	# 	pin (0,7)  side (A,B)
		try:
			if (pin<0 or pin>7) or (side!='A' and side!='B'):
				print ' --- MySwitch = GPIO.input(pin, side) ---'
				print ' --- pin (0 - 7)  side (A or B) ---'
				return;
			else:
				if side=='A':
					MySwitch = self.bus.read_byte_data(self.device_address, self.GPIOA)
					if MySwitch & (1<<pin) == (1<<pin):
						MySwitch=1
					else:
						MySwitch=0
				else:
					MySwitch = self.bus.read_byte_data(self.device_address, self.GPIOB)
					if MySwitch & (1<<pin) == (1<<pin):
						MySwitch=1
					else:
						MySwitch=0
	  
			return MySwitch;
		except:
			print ' --- Error accessing the chip MCP23017 ---'
			raise
