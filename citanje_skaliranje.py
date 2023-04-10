import serial
import numpy as np
import matplotlib.pyplot as plt

ser = serial.Serial("COM3", 9600)
lista = []
fs = 10
try:
    while True:
        line = ser.readline()
        vrednost = float(line.decode())
        vrednost = vrednost * 5.0 / 1023.0
        lista.append(vrednost)
        t = np.arrange(0,len(lista)/fs,1/fs)
        plt.figure()
        plt.plot(t,lista)
except KeyboardInterrupt:
    print('Doslo je do prekida.')
except:
    print('Neka druga greska.')
ser.close()
