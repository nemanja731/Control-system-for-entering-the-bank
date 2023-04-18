import serial

ser = serial.Serial("COM3", 9600)
ID1 = "ID of card is 83 fa 8d 20"
ID2 = "ID of card is 59 56 e4 5d"
print('Bring the card: ')
try:
    while True:
        line = ser.readline()
        current_ID = line.decode()
        if(ID2 == current_ID):
            print('Real card.')
        else:
            print('Wrong card.')
except KeyboardInterrupt:
    print("Keyboard break.")
except:
    print('Another kind of interruption.')
ser.close()