#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "Nome do WIFI";
const char* senha = "Senha do WIFI";
const String host = "https://projetoarduino.onrender.com/dados";

void setup() {
  Serial.begin(9600);

  WiFi.begin(ssid, senha);
  Serial.print("Conectando ao Wi-Fi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\n✅ Wi-Fi conectado.");
}

void loop() {
  if (Serial.available()) {
    String temp = Serial.readStringUntil('\n');
    temp.trim();

    if (WiFi.status() == WL_CONNECTED) {
      WiFiClientSecure client;
      client.setInsecure(); // ignora verificação SSL (funciona com HTTPS do Render)

      HTTPClient http;
      String url = host + "?temp=" + temp;

      http.begin(client, url);
      int codigo = http.GET();

      if (codigo > 0) {
        Serial.println("✅ Temperatura enviada: " + temp + " | Código HTTP: " + String(codigo));
      } else {
        Serial.println("❌ Erro HTTP: " + http.errorToString(codigo));
      }

      http.end();
    } else {
      Serial.println("⚠️ Wi-Fi desconectado.");
    }
  }
}
