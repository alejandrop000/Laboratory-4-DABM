int led = 10;

void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  }

void loop() {
  int ldr = analogRead(A0);
  Serial.println(ldr);

  if(Serial.available()){
      int x = Serial.read();
      analogWrite(led, x);
  }
}
