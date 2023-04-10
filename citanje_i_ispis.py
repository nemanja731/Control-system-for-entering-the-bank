import time
import serial

ser = serial.Serial("COM3", 9600)
try:
    while True:
        line = ser.readline();
        n = line.decode();
        print(int(n));
except KeyboardInterrupt:
    print('Doslo je do prekida.')
except:
    print('Doslo je do neke druge greske.')
ser.close()