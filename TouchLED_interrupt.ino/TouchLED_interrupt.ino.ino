int touchPin = 2;
volatile byte state = LOW;

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(touchPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(touchPin), blink, CHANGE);
}

void loop()
{
  // put your main code here, to run repeatedly:
}

void blink()
{
  state = !state;
  digitalWrite(LED_BUILTIN, state);
}
