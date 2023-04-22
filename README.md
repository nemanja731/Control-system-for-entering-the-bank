# Control system for entering the bank

<img src="https://static.wixstatic.com/media/e62e09_c2985c5cd99747e990e2ee0fdbfef162~mv2.gif" width="40%" height="40%" align="center"/>

The control system is simulated using three doors. Each door has a different opening system. There are three doors.

## First door :door:

You enter the waiting room through the first door by reading the RFID card. If the card exists in the database, the user is released, otherwise an alarm is triggered and the card's id is written to the _burglar.txt_ file.

## Second door :door:

Through the second door, one leaves the waiting room and enters the bank with the help of an interruption via a capacitive touch sensor. By pressing it, the break is activated and it is checked whether the first door is closed, which is simulated with the help of an ultrasonic sensor that measures the distance.

## Third door :door:

You exit the bank through the third door, and this is done by entering the exit code. Python and Arduino exchange data all the time using serial communication. :bank: :safety_vest:

Tools and programming languages ​​used: :toolbox:

- Python
- Arduino IDE with Serial communication
