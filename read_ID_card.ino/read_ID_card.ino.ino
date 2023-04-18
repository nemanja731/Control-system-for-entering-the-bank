#include <SPI.h>
#include <MFRC522.h>
#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);

void setup()
{
  Serial.begin(9600);
  SPI.begin();        // Initiate  SPI bus
  mfrc522.PCD_Init(); // Initiate MFRC522
  Serial.println("Read your card...");
  Serial.println();
}

void loop()
{
  if (!mfrc522.PICC_IsNewCardPresent())
  {
    return;
  }
  if (!mfrc522.PICC_ReadCardSerial())
  {
    return;
  }
  String content = "";
  for (byte i = 0; i < mfrc522.uid.size; i++)
  {
    content.concat(String(mfrc522.uid.uidByte[i], HEX));
    content.concat(" ");
  }
  Serial.print("ID of card is ");
  Serial.println(content);
}
