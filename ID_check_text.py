from threading import Thread
import serial
import time
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sys
import numpy as np

class App(QWidget):    
    def __init__(self):
        super().__init__()
        self.title = 'Check text'
        self.left = 200
        self.top = 200
        self.width = 120
        self.height = 190
        self.initUI()
        
    def initUI(self):   
        global data
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
         
        self.text_input = QLineEdit('ID', self)
        self.text_input.resize(100, 50)
        self.text_input.move(10,10)
        
        self.button = QPushButton('Start', self)
        self.button.resize(100,50)
        self.button.move(10,70)
        self.button.clicked.connect(self.button_fcn)
        
        self.text_output = QLabel(' ', self)
        self.text_output.resize(100, 50)
        self.text_output.move(10,130)   
        
        self.show()
        
    def button_fcn(self):
        # Telo funckije      
        
ser = serial.Serial("COM3", 9600)

def fun1():
    global data
    while True:
        data = ser.readline().decode()

def fun2():
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()

t1 = Thread(target = fun1)
t2 = Thread(target = fun2)
t1.start()
t2.start()


