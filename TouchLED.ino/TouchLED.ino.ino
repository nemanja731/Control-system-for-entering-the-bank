int touchPin = 7;
int touchVal = 0;

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(touchPin, INPUT);
}

void loop()
{
  touchVal = digitalRead(touchPin);
  if (touchVal == 1)
  {
    digitalWrite(LED_BUILTIN, HIGH);
  }
  else
  {
    digitalWrite(LED_BUILTIN, LOW);
  }
  delay(50);
}
