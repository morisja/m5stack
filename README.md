# Experiments with M5Stack

[m5stack](https://m5stack.com/) make some inexpensive esp32 based hardware.

Out of the box
[stick](https://www.tiktok.com/@aper0le/video/6875415250573724934?is_copy_url=0&is_from_webapp=v3&sender_device=pc&sender_web_id=6924108547886908933)
[stackcore](https://www.tiktok.com/@aper0le/video/6875691602472340742?is_copy_url=0&is_from_webapp=v3&sender_device=pc&sender_web_id=6924108547886908933)


## Setup
I am using PopOS.

Install the arduino package, download the arduino-cli, put it somewhere in your path (~/bin is in mine): 
```
apt-get install arduino
wget https://downloads.arduino.cc/arduino-cli/arduino-cli_latest_Linux_64bit.tar.gz
mkdir ~/bin
tar -xf arduino-cli_latest_Linux_64bit.tar.gz -C ~/bin
```

Init the arduino-cli, edit the file to include the board index, download:
```
$ arduino-cli config init

$ cat ~/.arduino15/arduino-cli.yaml 
board_manager:
  additional_urls:
    - https://dl.espressif.com/dl/package_esp32_index.json

$ arduino-cli core update-index
```

Connect your unit and verify it is found, make a note of the port, you will need it later:
```
$ arduino-cli  board list
Port         Type              Board Name FQBN Core
/dev/ttyUSB0 Serial Port (USB) Unknown             
```

For some reason my m5stick-c is not identified, it is however possible to specify the board type. 

Build the code:
```
$ cd helloworld
# note: the dir must include <dirname>.ino

$ arduino-cli compile --fqbn esp32:esp32:m5stick-c 
Sketch uses 386388 bytes (29%) of program storage space. Maximum is 1310720 bytes.
Global variables use 15476 bytes (4%) of dynamic memory, leaving 312204 bytes for local variables. Maximum is 327680 bytes.
```

Build and upload the code:
```
$ arduino-cli upload -p /dev/ttyUSB0 --fqbn esp32:esp32:m5stick-c
esptool.py v3.0-dev
Serial port /dev/ttyUSB0
Connecting......
Chip is ESP32-PICO-D4 (revision 1)
Features: WiFi, BT, Dual Core, 240MHz, Embedded Flash, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: 50:02:91:a2:76:dc
Uploading stub...
Running stub...
Stub running...
Changing baud rate to 1500000
Changed.
Configuring flash size...
Auto-detected Flash size: 4MB
Compressed 8192 bytes to 47...
Wrote 8192 bytes (47 compressed) at 0x0000e000 in 0.0 seconds (effective 16505.2 kbit/s)...
Hash of data verified.
Compressed 17120 bytes to 11166...
Wrote 17120 bytes (11166 compressed) at 0x00001000 in 0.1 seconds (effective 1038.1 kbit/s)...
Hash of data verified.
Compressed 389760 bytes to 211858...
Wrote 389760 bytes (211858 compressed) at 0x00010000 in 3.5 seconds (effective 901.1 kbit/s)...
Hash of data verified.
Compressed 3072 bytes to 128...
Wrote 3072 bytes (128 compressed) at 0x00008000 in 0.0 seconds (effective 6148.5 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
```

## Some examples
### helloworld
The most simple example I could write
### bounce
a square bouncing around the screen.
