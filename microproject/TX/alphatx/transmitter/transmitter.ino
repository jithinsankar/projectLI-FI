#define LED 3


void setup() {
    pinMode(LED, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    if (Serial.available()) {
        char serialListener = Serial.read();
        if (serialListener == 'H') {
            analogWrite(LED, 255);
        }
        if (serialListener == 'L') {
            analogWrite(LED, 0);
        }
    }
}
