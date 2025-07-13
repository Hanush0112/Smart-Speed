const int ENA = 9;
const int IN1 = 8;
const int IN2 = 7;

int speedValue = 0;

void setup() {
  Serial.begin(9600);
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);  // Forward direction
}

void loop() {
  if (Serial.available()) {
    String input = Serial.readStringUntil('\n');
    int detectedSpeed = input.toInt();

    // Map speed (20 to 100) to PWM (80 to 255)
    speedValue = map(detectedSpeed, 20, 100, 80, 255);
    speedValue = constrain(speedValue, 0, 255);  // safety

    analogWrite(ENA, speedValue);
    Serial.println("PWM set to: " + String(speedValue));
  }
}
