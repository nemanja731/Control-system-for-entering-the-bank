import sys
import serial
import time
from threading import Thread
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton

#trenutan broj ljudi u banci
brojLjudi = 0
sifra = "0517"
port = 'COM4'
v = 9600
#povezivanje sa serijskom komunikacijom
ser = serial.Serial(port, v)

#definicija klase
class App(QWidget):    
    def __init__(self):
        super().__init__()
        self.title = 'Kontrolni sistem za ulazak u banku'
        self.left = 750
        self.top = 400
        self.width = 500
        self.height = 300
        self.initUI()
    
    def initUI(self):
        global sifra
        global brojLjudi
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
                
        self.prikazID = QLabel('Id', self)
        self.prikazID.adjustSize()
        self.prikazID.move(25,100)
                
        self.prikazObavestenja = QLabel('Obavestenja', self)
        self.prikazObavestenja.adjustSize()
        self.prikazObavestenja.move(250, 30)
        
        self.prikazUneteSifre = QLabel('Sifra', self)
        self.prikazUneteSifre.adjustSize()
        self.prikazUneteSifre.move(250,130)
        
        self.prikazBrojaLjudi = QLabel('Broj ljudi u banci je ' + str(brojLjudi), self)
        self.prikazBrojaLjudi.adjustSize()
        self.prikazBrojaLjudi.move(25, 150)
                
        self.unetaSifra = QLineEdit('', self)
        self.unetaSifra.setDisabled(True)
        self.unetaSifra.adjustSize()
        self.unetaSifra.move(250,150)
                
        self.dugmeIzlazAplikacije = QPushButton('Izlaz iz\naplikacije', self)
        self.dugmeIzlazAplikacije.adjustSize()
        self.dugmeIzlazAplikacije.move(375,230)
        self.dugmeIzlazAplikacije.clicked.connect(self.fjaIzlazAplikacije)
        
        self.dugmeIzlazBanke = QPushButton('Izlaz iz\nbanke', self)
        self.dugmeIzlazBanke.adjustSize()
        self.dugmeIzlazBanke.move(250,230)
        self.dugmeIzlazBanke.setDisabled(True)
        self.dugmeIzlazBanke.clicked.connect(self.fjaIzlazBanke)      
               
        self.azuriranje()
        self.show()
    
    #funkcija odgovorna za izlazak iz banke    
    def fjaIzlazBanke(self):
        global brojLjudi
        global pogresnaSifra
        if (sifra == self.unetaSifra.text()):
            self.prikazObavestenja.setText('Korisnik je izasao iz banke')
            self.prikazObavestenja.adjustSize()
            if(brojLjudi > 0):
                brojLjudi -= 1
            self.prikazBrojaLjudi.setText('Broj ljudi u banci je  ' + str(brojLjudi))
            operacija = str(brojLjudi) + '\n'
            ser.write(operacija.encode())  
            pogresnaSifra = False
        else:
            self.prikazObavestenja.setText('Pogresna sifra, pokusajte ponovo.')
            self.prikazObavestenja.adjustSize()
            operacija = 'stop\n'
            ser.write(operacija.encode())
            operacija = 'svetliCrveno\n'
            ser.write(operacija.encode())
            pogresnaSifra = True
            self.dugmeIzlazBanke.setDisabled(False)
        if(brojLjudi == 0):
              self.dugmeIzlazBanke.setDisabled(True)
              self.unetaSifra.setDisabled(True)    
    
    #funkcija odgovorna za izlazak iz aplikacije
    def fjaIzlazAplikacije(self):
        #gasimo lampice kao i serijsku komunikaciju
        operacija = 'stop\n'
        ser.write(operacija.encode())
        QApplication.quit()
        ser.close()
        print('Uspesno ste izasli iz aplikacije.')
    
    #funkcija odgovorna za azuriranje
    def azuriranje(self):
        self.prikazID.adjustSize()
        self.prikazObavestenja.adjustSize()
        self.prikazUneteSifre.adjustSize()
        self.unetaSifra.adjustSize()
        self.prikazBrojaLjudi.setText('Broj ljudi u banci je  ' + str(brojLjudi))
        self.prikazBrojaLjudi.adjustSize()
        self.dugmeIzlazAplikacije.adjustSize()
        self.dugmeIzlazBanke.adjustSize()

#funkcija main odgovorna za pokretanje grafickog interfejsa
def main():
    app = QApplication(sys.argv)
    global ex
    ex = App()
    app.exec_()

#funkcija odgovorna za senzor dodira
def senzorDodira():
    global ex
    global brojLjudi
    try:
        rastojanje = 0
        while True:
            operacija = ''
            procitanaOperacija = ser.readline().decode()
            if(procitanaOperacija == "Rastojanje je \r\n"):
                rastojanje = int(ser.readline().decode())
                print('Rastojanje je ' + str(rastojanje))
            elif(procitanaOperacija[0:5] == "Dodir"):
                if(rastojanje < 10):
                    operacija = 'svetliZeleno\n'
                    ser.write(operacija.encode())
                    time.sleep(0.5)
                    ex.prikazObavestenja.setText('Ulazak u banku odobren!')
                    ex.unetaSifra.setDisabled(False)
                    ex.dugmeIzlazBanke.setDisabled(False)
                    brojLjudi += 1
                    ex.prikazBrojaLjudi.setText('Broj ljudi u banci je  ' + str(brojLjudi))
                    operacija = str(brojLjudi)
                    operacija +='\n'
                    ser.write(operacija.encode())
                    time.sleep(2)
                    break
                
    #hvatamo izuzetke
    #gasimo lampice kao i serijsku komunikaciju
    except KeyboardInterrupt:
        operacija = 'stop\n'
        ser.write(operacija.encode())
        ser.close()
            
    except Exception:
        op = 'stop\n'
        ser.write(op.encode())
        ser.close()
        print("Greska!")
        
#funkcija obrade pristupa kartice, kao i komunikacije sa arduinom            
def obradaKartice():
    global ex
    global pogresnaSifra
    pogresnaSifra = False
    try:
        trenutniID = ''
        maksLjudi = 0
        while (True):
            #ukoliko je korisnik uneo pogresnu sifru cekamo u ovoj while petlji ponovan unos
            while pogresnaSifra:
                time.sleep(1)
            procitanaOperacija = ser.readline().decode()
            print('Dozvoljen broj ljudi je ' + str(maksLjudi))
            if(brojLjudi < maksLjudi):   
                 if(pogresnaSifra == False):
                    ex.prikazObavestenja.setText('Ocitajte karticu')
                #ex.prikazObavestenja.adjustSize()
            else:
                ex.prikazObavestenja.setText('Dostignut je maksimalan\n broj ljudi u banci')
                ex.prikazObavestenja.adjustSize()
            if(brojLjudi < maksLjudi and procitanaOperacija == "Id je\r\n"):
                trenutniID = ser.readline().decode()
                operacija = 'stop\n'
                ser.write(operacija.encode())
                baza = open('IDbaza.txt', 'r')
                #u slucaju da id kartice ima manje karaktera od standardnih, tada ona ima spejs na kraju
                if (trenutniID[len(trenutniID) - 3] == ' '):
                     pomocni = trenutniID[0 : len(trenutniID) - 3]
                else:
                    pomocni = trenutniID[0 : len(trenutniID) - 2]
                #trazimo da li se ucitana kartica nalazi u bazi
                nadjen = False
                for linija in baza:
                    if (pomocni == linija[0 : len(linija) - 1]):
                        nadjen = True
                        break
                #nalazi se
                if nadjen:
                    ex.prikazID.setText('Id je ' + str(trenutniID))
                    ex.prikazObavestenja.setText('Kartica je ocitana.\nDodirnite senzor dodira.')
                    ex.azuriranje()
                    senzorDodira()
                #ne nalazi se
                else:
                    operacija = 'svetliCrveno\n'
                    ser.write(operacija.encode())
                    ex.prikazObavestenja.setText('Imamo provalnika!\n')
                    ex.azuriranje()
                    time.sleep(0.5)
                    provalnik = open('provalnik.txt', 'a')
                    vreme = time.localtime()
                    trenutnoVreme = time.strftime("%H:%M:%S", vreme)
                    provalnik.write('Id provalnika je ' + str(trenutniID))
                    provalnik.write(trenutnoVreme)
                    provalnik.write("\n\n")
                    provalnik.close()
                baza.close() 
            elif(procitanaOperacija == "Dozvoljen broj ljudi:\r\n"):
                maksLjudi = int(ser.readline().decode())
            ex.azuriranje()
              
    #hvatamo izuzetke
    #gasimo lampice kao i serijsku komunikaciju       
    except KeyboardInterrupt:
        operacija = 'stop\n'
        ser.write(operacija.encode())
        ser.close()
            
    except Exception:
        op = 'stop\n'
        ser.write(op.encode())
        ser.close()
        print("Greska!")
        

#petlje
t1 = Thread(target = main)
t2 = Thread(target = obradaKartice)
t1.start()
t2.start()