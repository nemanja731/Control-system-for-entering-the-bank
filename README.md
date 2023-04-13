# Sistem-za-ulaz-u-banku

Program simulates bank entrancing and keeps records of people in a bank using RFID cards
and touch sensor that are connected to Arduino.

The bank entry system is simulated. There are three doors. Through the first door you enter the waiting room. Through the second door you exit the waiting room and enter the bank. Through the third door you exit the bank. The first door is opened with the RFID card only if the card is in the base, otherwise the alarm is activated. The second door is opened by a capacitive touch sensor and can only be opened if the first one is closed, which is measured by an ultrasonic sensor that measures the distance. The third door is opened with the correctly code entered. The program uses interrupts to regulate the system. :bank:

Used programming languages ​​and tools :toolbox::

- Python
- Arduino IDE with Serial communication
