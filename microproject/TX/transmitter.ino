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
        else if (serialListener == 'L') {
            analogWrite(LED, 50);
        }
        else if (serialListener == 'M') {
            analogWrite(LED, 100);
        }
    }
}
