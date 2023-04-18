String inputString = "";
String operation = "stop";
int voltage = 0;

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  if (operation == "start")
  {
    voltage = analogRead(A0);
    Serial.println(voltage);
    delay(1000);
  }
  else if (operation == "stop")
  {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(500);
    digitalWrite(LED_BUILTIN, LOW);
    delay(500);
  }
  else
  {
    Serial.println("Input error! The program returns to the waiting state.");
    operation = "stop";
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
