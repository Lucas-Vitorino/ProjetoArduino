#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <math.h>  // Necessário para log()

#define RELE 8
#define SENSOR_TEMP A2

const int tempMin = 22;  // Temperatura mínima para desligar o relé
const int tempMax = 28;  // Temperatura máxima para ligar o relé

LiquidCrystal_I2C lcd(0x27, 16, 2); // Endereço I2C do seu módulo LCD (0x27 ou 0x3F)

void setup() {
  pinMode(RELE, OUTPUT);
  digitalWrite(RELE, HIGH); // Inicia com relé desligado

  lcd.init();
  lcd.backlight();

  lcd.setCursor(0, 0);
  lcd.print("Iniciando...");
  delay(1000);
  lcd.clear();
}

void loop() {
  int leitura = analogRead(SENSOR_TEMP);

  // Conversão de leitura para temperatura em Celsius (NTC 10k + resistor 10k)
  float resistencia = (1023.0 / leitura - 1.0) * 10000.0;
  float temperaturaK = 1.0 / (0.001129148 + 0.000234125 * log(resistencia) + 0.0000000876741 * pow(log(resistencia), 3));
  float temperatura = temperaturaK - 273.15;

  // Controle automático com histerese
  static bool ligado = false;

  if (temperatura >= tempMax && !ligado) {
    digitalWrite(RELE, LOW); // Liga o relé
    ligado = true;
  } else if (temperatura <= tempMin && ligado) {
    digitalWrite(RELE, HIGH); // Desliga o relé
    ligado = false;
  }

  // Atualiza LCD
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print((int)temperatura);
  lcd.print((char)223);  // símbolo °C
  lcd.print("C    ");

  lcd.setCursor(0, 1);
  lcd.print("Sistema: ");
  lcd.print(ligado ? "ON " : "OFF");

  delay(500);
}
