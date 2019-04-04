"""
https://www.instructables.com/id/Interface-Python-and-Arduino-with-pySerial/
"""
from time import sleep
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600) # Establish the connection on a specific port
for counter in range(32,128): # Below 32 and above 128 everything in ASCII is gibberish
     ser.write(str(chr(counter))) # Convert the decimal number to ASCII then send it to the Arduino
     print ser.readline() # Read the newest output from the Arduino
     sleep(.1) # Delay for one tenth of a second
    
