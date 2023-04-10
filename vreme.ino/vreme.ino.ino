#include<TimerOne.h>

int brojac = 0;
bool stanje = false;

void setup() {
  Serial.begin(9600);
  Timer1.initialize(1000000);
  Timer1.attachInterrupt(timerIsr);
}

void loop() {
  if(stanje == true) {
    Serial.println(brojac);
    stanje = false;
  }

}

void timerIsr() {
  brojac += 1;
  stanje = true;
}
