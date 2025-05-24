#include <SoftwareSerial.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

SoftwareSerial esp(2, 3); // RX, TX
LiquidCrystal_I2C lcd(0x27, 16, 2); 

const int sensorNTC = A2;
const int rele = 8; // pino que aciona o relé
const float TEMP_MIN = 22.0;
const float TEMP_MAX = 26.0;

void setup() {
  Serial.begin(9600);
  esp.begin(9600);
  lcd.begin(16, 2);
  lcd.backlight();

  pinMode(rele, OUTPUT);
  digitalWrite(rele, HIGH); // relé desligado inicialmente

  lcd.setCursor(0, 0);
  lcd.print("Iniciando...");
  delay(2000);
}

void loop() {
  int leitura = analogRead(sensorNTC);
  float resistencia = (1023.0 / leitura - 1.0) * 10000.0;
  float temperatura = 1.0 / (log(resistencia / 10000.0) / 3950.0 + 1.0 / 298.15) - 273.15;

  // Envia para ESP-01
  esp.println(temperatura);
  Serial.println("Temperatura enviada: " + String(temperatura));

  // Exibe no LCD
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(temperatura, 1);
  lcd.print(" C");

  // Controle do ar-condicionado
  if (temperatura >= TEMP_MAX) {
    digitalWrite(rele, LOW); // liga
    lcd.setCursor(0, 1);
    lcd.print("AC ON (quente)");
  } else if (temperatura <= TEMP_MIN) {
    digitalWrite(rele, HIGH); // desliga
    lcd.setCursor(0, 1);
    lcd.print("AC OFF (frio)");
  } else {
    lcd.setCursor(0, 1);
    lcd.print("AC MODO ESTAVEL ");
  }

  delay(15000); // lê a cada 15 segundos
}
