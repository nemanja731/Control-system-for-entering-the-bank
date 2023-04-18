import serial

ser = serial.Serial("COM3", 9600)
i = 0
while i <= 30:
    line = ser.readline();
    n = line.decode();
    print(int(n));
    i += 1;
ser.close();
    