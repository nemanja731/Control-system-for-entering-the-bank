#include <TimerOne.h>

int counter = 0;
bool state = false;

void setup()
{
  Serial.begin(9600);
  Timer1.initialize(1000000);
  Timer1.attachInterrupt(timerIsr);
}

void loop()
{
  if (state == true)
  {
    Serial.println(counter);
    state = false;
  }
}

void timerIsr()
{
  counter += 1;
  state = true;
}
