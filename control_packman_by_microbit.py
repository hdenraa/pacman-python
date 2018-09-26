import sys, serial, time
from random import randint
import re
print(sys.version)
port = "/dev/ttyACM0"
baud = 115200
sumx = 0
sumy = 0  
count=0  

while True:

    s = serial.Serial(port)
    s.baudrate = baud
    s.parity = serial.PARITY_NONE
    s.databits = serial.EIGHTBITS
    s.stopbits = serial.STOPBITS_ONE
    data = s.readline()
    time.sleep(0.01)
    data = str(data)
    print(data)

    if "x, y, z:" in data:
        count += 1 
        split = data.split(":")[-1].split()
        print(split)
        x = int(split[0])
        y = int(split[1])
        z = int(re.sub('[^-0-9]', '',split[2]))
        print("New x, y, z:", x, y, z)
        sumx += x
        sumy += y

print("sumx,sumy:", sumx,sumy)
