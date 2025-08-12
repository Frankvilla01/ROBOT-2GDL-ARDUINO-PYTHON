#include <Servo.h>

Servo servo1;
Servo servo2;

int angulo1 = 90;
int angulo2 = 90;

void setup() {
  Serial.begin(9600);
  servo1.attach(9);  // Pin del servo 1
  servo2.attach(10); // Pin del servo 2
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read();
    
    if (comando == 'U') {
      angulo2 += 10;
    } else if (comando == 'D') {
      angulo2 -= 10;
    } else if (comando == 'L') {
      angulo1 += 10;
    } else if (comando == 'R') {
      angulo1 -= 10;
    } else if (comando == 'A') {
      int nuevo_angulo1 = Serial.parseInt();
      int nuevo_angulo2 = Serial.parseInt();
      
      angulo1 = constrain(nuevo_angulo1, 0, 180);
      angulo2 = constrain(nuevo_angulo2, 0, 180);
    }
    
    angulo1 = constrain(angulo1, 0, 180);
    angulo2 = constrain(angulo2, 0, 180);
    
    moverServos(angulo1, angulo2);
  }
}

void moverServos(int ang1, int ang2) {
  servo1.write(ang1);
  servo2.write(ang2);
  delay(100);  // Espera para asegurar que el servo se mueva completamente
}
