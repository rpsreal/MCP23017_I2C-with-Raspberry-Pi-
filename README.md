# MCP23017_I2C-with-Raspberry-Pi-
Python library to control the MCP23017 GPIO

Install this first:
sudo apt-get install -y python-smbus i2c-tools

[Wiring](https://cld.pt/dl/download/04feb1aa-89dd-44ad-ab2b-31cc3bd9637e/Chip.jpg)

With this library you can use the chip with simple commands, like:
-  GPIO.setup( 0, 'OUT', 'A') to configure GPA0 like output
-  GPIO.output(0, 1, 'A') to write in GPA0 1 (high)
-  switch = GPIO.input(7, 'B') to save the state of GPB7 in 'switch'
