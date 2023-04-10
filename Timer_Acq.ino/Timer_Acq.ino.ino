#include<TimerOne.h>

volatile int voltage = 0;
volatile byte state = 0;

void setup() {
  Serial.begin(9600);
  Timer1.initialize(1000000);
  Timer1.attachInterrupt(timerIsr);

}

void loop() {
  if(state) {
    Serial.println(voltage);
    state = 0;
  }
}

void timerIsr() {
  state = 1;
  voltage = analogRead(A0);
}
