# Control system for entering the bank

<img src="https://static.wixstatic.com/media/e62e09_c2985c5cd99747e990e2ee0fdbfef162~mv2.gif" width="40%" height="40%" align="center"/>

The control system is simulated using a safety doors. Each door has a different opening system. There are three doors.

## First door :door:

By reading the RFID card, you can pass through the first door and enter the waiting room. If the card exists in the database, the user is released, otherwise an alarm is triggered and the card's id is written to the _burglar.txt_ file.

## Second door :door:

With the help of interruption via the capacitive touch sensor, it is possible to pass through other doors. This leaves the waiting room and enters the bank. By pressing it, the break is activated and it is checked whether the first door is closed, which is simulated with the help of an ultrasonic sensor that measures the distance.

## Third door :door:

By entering the exit code, you pass through the third door and exit the bank. Python and Arduino exchange data all the time using serial communication. :bank: :safety_vest:

Tools and programming languages ​​used: :toolbox:

- Python
- Arduino IDE with Serial communication
