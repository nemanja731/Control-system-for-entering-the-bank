import time
import serial

ser = serial.Serial("COM3", 9600)
try:
    while True:
        line = ser.readline();
        n = line.decode();
        print(int(n));
except KeyboardInterrupt:
    print('There was an interruption.')
except:
    print('Another error occurred.')
ser.close()