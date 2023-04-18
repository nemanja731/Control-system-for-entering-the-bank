#include <TM1637Display.h>

const int CLK = 9;
const int DIO = 8;
int NumStep = 0;
TM1637Display display(CLK, DIO);

void setup()
{
  display.setBrightness(7);
}

void loop()
{
  for (NumStep = 0; NumStep < 9999; NumStep++)
  {
    display.showNumberDec(NumStep);
    delay(300);
  }
}
