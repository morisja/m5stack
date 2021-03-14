.SILENT: 
all:
	gifsicle --resize-height 80 spongebob-large.gif -o spongebob-small.gif
	./env/bin/python3 gif2c.py
	arduino-cli compile --fqbn esp32:esp32:m5stick-c 

upload: all 
	arduino-cli upload -p /dev/ttyUSB0 --fqbn esp32:esp32:m5stick-c

