void setup() {
  // put your setup code here, to run once:
Serial.begin(19200);
}
int ldrpin=A0;
void loop() {
  // put your main code here, to run repeatedly:
Serial.println(int(analogRead(ldrpin)));
delay(1000);
}
