# MCP23017_I2C-with-Raspberry-Pi-
Python library to control the MCP23017 GPIO

Install this first:
sudo apt-get install -y python-smbus i2c-tools

Wiring
![alt text](https://cld.pt/dl/download/53a9d98a-c33e-407a-9480-a237ce9e8351/esquema.png)

With this library you can use the chip with simple commands, like:
-  GPIO.setup( 0, 'OUT', 'A')     # to configure GPA0 like output
-  GPIO.output(0, 1, 'A')         # to write in GPA0 1 (high)
-  switch = GPIO.input(7, 'B')    # to save the state of GPB7 in 'switch'




Developed by Rui Pedro Silva; Portugal; 03/2015
Based on the work of http://www.raspberrypi-spy.co.uk
