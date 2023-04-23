
#include <Servo.h>


Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 90;    // variable to store the servo position

void setup() {
  
  Serial.begin(9600);
  myservo.attach(14);  // attaches the servo on pin 9 to the servo object
  myservo.write(pos); 
  }

void loop() {
 if (Serial.available())
 {
  String a = Serial.readString();
  Serial.println(a);
  int b = a.toInt();
  myservo.write(90 - b);
  delay(15);
  }
}
