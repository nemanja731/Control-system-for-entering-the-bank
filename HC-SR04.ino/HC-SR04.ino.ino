long duration;
long distance;
int trigPin = 9;
int echoPin = 10;

void setup()
{
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop()
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = 17.0 * duration / 1000.0;
  Serial.print("Distance = ");
  Serial.print(distance);
  Serial.println(" cm");
  delay(500);
}
