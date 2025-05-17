#include <LiquidCrystal.h>
#include <Thermistor.h>

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

Thermistor temp(A2);

const int RelePin = 8;
const int tempMin = 25;
const int tempMax = 27;

bool ligado = false; // Estado atual do "ar-condicionado"

void setup() {
  lcd.begin(16, 2);
  pinMode(RelePin, OUTPUT);
  digitalWrite(RelePin, HIGH); // Desliga o relé no início
  lcd.setCursor(0, 0);
  lcd.print("Temp agora:");
}

void loop() {
  int temperatura = temp.getTemp();

  // Atualiza LCD com temperatura
  lcd.setCursor(0, 1);
  lcd.print(temperatura);
  lcd.print((char)223);
  lcd.print("C ");

  // Lógica com histerese
  if (temperatura >= tempMax && !ligado) {
    ligado = true;
    digitalWrite(RelePin, LOW);
  } else if (temperatura <= tempMin && ligado) {
    ligado = false;
    digitalWrite(RelePin, HIGH);
  }

  // Exibe status
  lcd.setCursor(10, 1);
  if (ligado) {
    lcd.print("ON ");
  } else {
    lcd.print("OFF");
  }

  delay(1000);
}
