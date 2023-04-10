long trajanje;
long rastojanje;
int trigPin = 9;
int echoPin = 10;

void setup() {
  pinMode(trigPin,OUTPUT);
  pinMode(echoPin,INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigPin,LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin,LOW);
  trajanje = pulseIn(echoPin,HIGH);
  rastojanje = 17.0*trajanje/1000.0;
  Serial.print("Rastojanje = ");
  Serial.print(rastojanje);
  Serial.println(" cm");
  delay(500);
}
