# Kontrolni-sistem-za-ulaz-u-banku

The control system for entering the bank using three doors is simulated.

## First door

You enter the waiting room through the first door by reading the RFID card. If the card exists in the database, the user is released, otherwise an alarm is triggered and the card's id is written to the _burglar.txt_ file.

## Second door

Through the second door, one leaves the waiting room and enters the bank with the help of an interruption via a capacitive touch sensor. By pressing it, the break is activated and it is checked whether the first door is closed, which is simulated with the help of an ultrasonic sensor that measures the distance.

## Third door

You exit the bank through the third door, and this is done by entering the exit code. Python and Arduino exchange data all the time using serial communication. :bank: :safety_vest:

Tools and programming languages ​​used: :toolbox:

- Python
- Arduino IDE with Serial communication
