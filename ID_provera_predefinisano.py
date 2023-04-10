import serial

ser = serial.Serial("COM3", 9600)
ID1 = "ID kartice je 83 fa 8d 20"
ID2 = "ID kartice je 59 56 e4 5d"
print('Prinesite karticu: ')
try:
    while True:
        line = ser.readline()
        ID_tren = line.decode()
        if(ID2 == ID_tren):
            print('Prava kartica.')
        else:
            print('Pogresna kartica')
except KeyboardInterrupt:
    print("Prekid tastaturom.")
except:
    print('Druga vrsta prekida.')
ser.close()