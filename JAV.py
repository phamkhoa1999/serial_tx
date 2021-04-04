import serial
import time

port = 'COM8'
baud = 115200

ser = serial.Serial(port, baud, timeout=1)

if ser.isOpen():
	print(ser.name + ' is_open...')

while(1):
        #out = ser.readlines(1)
        #if out != []:
         #   print(out)
        frame = "vel " + "9.5 9.5 1.57 0.0 0.0 0.0"
        frame1 = frame.encode('UTF-8')
        print(frame + "--" + str(len(frame)))
        ser.write(frame1)
        time.sleep(1)
 
