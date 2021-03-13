.SILENT: 
all:
	arduino-cli compile --fqbn esp32:esp32:m5stick-c 

upload: all 
	arduino-cli upload -p /dev/ttyUSB0 --fqbn esp32:esp32:m5stick-c
