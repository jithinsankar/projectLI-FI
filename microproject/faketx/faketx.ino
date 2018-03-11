#define LED 3
void setup() {
  // put your setup code here, to run once:

pinMode(LED, OUTPUT);
    Serial.begin(1200);


}

void loop() {
  // put your main code here, to run repeatedly:
  analogWrite(LED, 255);
    delay(1000);
    analogWrite(LED, 0);
    delay(1000);

}
