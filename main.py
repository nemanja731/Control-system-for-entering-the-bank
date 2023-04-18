import sys
import serial
import time
from threading import Thread
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton

#the current number of people in the bank
numberOfPeople = 0
password = "0517"
port = 'COM4'
v = 9600
#connecting to serial communication
ser = serial.Serial(port, v)

#class definition
class App(QWidget):    
    def __init__(self):
        super().__init__()
        self.title = 'Control system for entering the bank'
        self.left = 750
        self.top = 400
        self.width = 500
        self.height = 300
        self.initUI()
    
    def initUI(self):
        global password
        global numberOfPeople
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)  
        self.setupLabels()     
        self.setupLineEdit()   
        self.setupButtons()      
        self.updating()
        self.show()

    def setupLineEdit(self):
        self.enteredPassword = QLineEdit('', self)
        self.enteredPassword.setDisabled(True)
        self.enteredPassword.adjustSize()
        self.enteredPassword.move(250,150)

    def setupLabels(self):
        self.displayID = QLabel('ID', self)
        self.displayID.adjustSize()
        self.displayID.move(25,100)
                
        self.displayNotification = QLabel('Notifications', self)
        self.displayNotification.adjustSize()
        self.displayNotification.move(250, 30)
        
        self.displayOfTheEnteredPassword = QLabel('password', self)
        self.displayOfTheEnteredPassword.adjustSize()
        self.displayOfTheEnteredPassword.move(250,130)
        
        self.displayNumberOfPeople = QLabel('Number of people in bank is ' + str(numberOfPeople), self)
        self.displayNumberOfPeople.adjustSize()
        self.displayNumberOfPeople.move(25, 150)

    def setupButtons(self):
        self.exitButton = QPushButton('Exit from\napplication', self)
        self.exitButton.adjustSize()
        self.exitButton.move(375,230)
        self.exitButton.clicked.connect(self.functionToExitApp)
        
        self.exitBankButton = QPushButton('Exit from\nbank', self)
        self.exitBankButton.adjustSize()
        self.exitBankButton.move(250,230)
        self.exitBankButton.setDisabled(True)
        self.exitBankButton.clicked.connect(self.functionToExitBank)
    
    #function responsible for exiting the bank  
    def functionToExitBank(self):
        global numberOfPeople
        global wrongPassword
        if (password == self.enteredPassword.text()):
            self.displayNotification.setText('The user has left the bank')
            self.displayNotification.adjustSize()
            if(numberOfPeople > 0):
                numberOfPeople -= 1
            self.displayNumberOfPeople.setText('Number of people in bank is ' + str(numberOfPeople))
            operation = str(numberOfPeople) + '\n'
            ser.write(operation.encode())  
            wrongPassword = False
        else:
            self.displayNotification.setText('Wrong password, try again.')
            self.displayNotification.adjustSize()
            operation = 'stop\n'
            ser.write(operation.encode())
            operation = 'redLightOn\n'
            ser.write(operation.encode())
            wrongPassword = True
            self.exitBankButton.setDisabled(False)
        if(numberOfPeople == 0):
            self.exitBankButton.setDisabled(True)
            self.enteredPassword.setDisabled(True)    
    
    #function responsible for exiting the app
    def functionToExitApp(self):
        #turn off the lights as well as the serial communication
        operation = 'stop\n'
        ser.write(operation.encode())
        QApplication.quit()
        ser.close()
        print('Uspesno ste izasli iz aplikacije.')
    
    #function responsible for updating
    def updating(self):
        self.displayID.adjustSize()
        self.displayNotification.adjustSize()
        self.displayOfTheEnteredPassword.adjustSize()
        self.enteredPassword.adjustSize()
        self.displayNumberOfPeople.setText('Number of people in bank is  ' + str(numberOfPeople))
        self.displayNumberOfPeople.adjustSize()
        self.exitButton.adjustSize()
        self.exitBankButton.adjustSize()

    def processTouch(self, distance):
        operation = ''
        readOperation = ser.readline().decode()
        if(readOperation == "Distance is \r\n"):
            distance = int(ser.readline().decode())
            print('Distance is ' + str(distance))
        elif(readOperation[0:5] == "Touch"):
            if(distance < 10):
                operation = 'greenLightOn\n'
                ser.write(operation.encode())
                time.sleep(0.5)
                ex.displayNotification.setText('Bank entry approved!')
                ex.enteredPassword.setDisabled(False)
                ex.exitBankButton.setDisabled(False)
                numberOfPeople += 1
                ex.displayNumberOfPeople.setText('Number of people in bank is  ' + str(numberOfPeople))
                operation = str(numberOfPeople)
                operation +='\n'
                ser.write(operation.encode())
                time.sleep(2)
                return False
        return True

    #the function responsible for the touch sensor
    def touchSensor(self):
        global ex
        global numberOfPeople
        try:
            distance = 0
            flag = True
            while flag:
                flag = self.processTouch(distance)
                    
        #catch exceptions
        #turn off the lights as well as serial communication     
        except KeyboardInterrupt:
            operation = 'stop\n'
            ser.write(operation.encode())
            ser.close()
                
        except Exception:
            op = 'stop\n'
            ser.write(op.encode())
            ser.close()
            print("Error!")
            
    #function responsible for card access processing and communication with arduino         
    def processCards(self):
        global ex
        global wrongPassword
        wrongPassword = False
        try:
            self.process(ex)
                
        #catch exceptions
        #turn off the lights as well as serial communication     
        except KeyboardInterrupt:
            operation = 'stop\n'
            ser.write(operation.encode())
            ser.close()
                
        except Exception:
            op = 'stop\n'
            ser.write(op.encode())
            ser.close()
            print("Error!")

    #initialize for process
    def initialize(self, maxPeople, ex):
        #if the user entered the wrong password, we wait in this while loop for re-entry
        while wrongPassword:
            time.sleep(1)
        readOperation = ser.readline().decode()
        print('The number of people allowed is ' + str(maxPeople))
        if(numberOfPeople < maxPeople):   
            if(wrongPassword == False):
                ex.displayNotification.setText('Read the card')
                #ex.displayNotification.adjustSize()
        else:
            ex.displayNotification.setText('The maximum number of people\nin the bank has been reached')
            ex.displayNotification.adjustSize()
        return readOperation

    #process card
    def process(self, ex):
        currentID = ''
        maxPeople = 0
        while (True):
            readOperation = self.initialize(maxPeople, ex)
            if(numberOfPeople < maxPeople and readOperation == "ID is\r\n"):
                currentID = ser.readline().decode()
                operation = 'stop\n'
                ser.write(operation.encode())
                base = open('IDbase.txt', 'r')
                #in case the ID card has fewer characters than the standard ones, then it has a space at the end
                if (currentID[len(currentID) - 3] == ' '):
                    auxiliary = currentID[0 : len(currentID) - 3]
                else:
                    auxiliary = currentID[0 : len(currentID) - 2]
                #it is asked whether the loaded card is in the database
                found = False
                for line in base:
                    if (auxiliary == line[0 : len(line) - 1]):
                        found = True
                        break
                self.checkIfIDIsFound(ex, currentID, found)
                base.close() 
            elif(readOperation == "Number of people allowed is :\r\n"):
                maxPeople = int(ser.readline().decode())
            ex.updating()

    def checkIfIDIsFound(self, ex, currentID, found):
        #located
        if found:
            ex.displayID.setText('ID is ' + str(currentID))
            ex.displayNotification.setText('The card has been read.\nTouch the Touch sensor.')
            ex.updating()
            self.touchSensor()
        #not located
        else:
            operation = 'redLightOn\n'
            ser.write(operation.encode())
            ex.displayNotification.setText('We have a burglar!\n')
            ex.updating()
            time.sleep(0.5)
            burglar = open('burglar.txt', 'a')
            vreme = time.localtime()
            currentTime = time.strftime("%H:%M:%S", vreme)
            burglar.write('ID of burglar is ' + str(currentID))
            burglar.write(currentTime)
            burglar.write("\n\n")
            burglar.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    global ex
    ex = App()
    app.exec_()
    t = Thread(target = ex.processCards)
    t.start()