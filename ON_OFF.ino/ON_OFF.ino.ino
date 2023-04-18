String inputString = "";
String operation = "OFF";

void setup()
{
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
  if (operation == "ON")
  {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(1000);
  }
  else if (operation == "OFF")
  {
    digitalWrite(LED_BUILTIN, LOW);
    delay(1000);
  }
}

void serialEvent()
{
  while (Serial.available())
  {
    char inChar = (char)Serial.read();
    if (inChar == '\n')
    {
      operation = inputString;
      inputString = "";
    }
    else
    {
      inputString += inChar;
    }
  }
}
