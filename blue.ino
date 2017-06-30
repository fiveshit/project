#include <SotfwareSerial.h>

SotfwareSerial BT(8,9);//RX,TX

char chr_val;

void setup()
{
    serial.begin(38400);
    Serial.println("Rright!");
    BT.begin(38400);
}
void loop()
{
  if(Serial.available())
  {
      chr_val = Serial.read();
      BT.print(chr_val);
  }
  if(BT.available())
  {
      chr_val = BT.read();
      Serial.print(chr_val);
  }
}
