import serial
import numpy as np
import matplotlib.pyplot as plt

ser = serial.Serial("COM3", 9600)
list = []
fs = 10
try:
    while True:
        line = ser.readline()
        value = float(line.decode())
        value = value * 5.0 / 1023.0
        list.append(value)
        t = np.arrange(0,len(list)/fs,1/fs)
        plt.figure()
        plt.plot(t,list)
except KeyboardInterrupt:
    print('There was an interruption.')
except:
    print('Some other error.')
ser.close()
