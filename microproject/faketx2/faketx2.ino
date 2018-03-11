#define LED 3
void setup() {
  // put your setup code here, to run once:

pinMode(LED, OUTPUT);
    Serial.begin(1200);
  analogWrite(LED, 255);//s
    delay(1000);
    analogWrite(LED, 0);
    delay(1000);
     analogWrite(LED, 255);
    delay(4000);
       analogWrite(LED, 0);
    delay(1000);
analogWrite(LED, 255);//s
    delay(2000);
       analogWrite(LED, 0);
    delay(5000);
      analogWrite(LED, 255);//s
    delay(2000);
        analogWrite(LED, 0);
    delay(1000);
          analogWrite(LED, 255);
    delay(1000);
        analogWrite(LED, 0);
    delay(3000);
         analogWrite(LED, 255);
    delay(1000);
            analogWrite(LED, 0);
    delay(6000);

}

void loop() {
  // put your main code here, to run repeatedly:

}
