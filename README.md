# 🧠 Projeto: Monitor de Temperatura com Arduino, ESP-01 e Visualização Remota

Este projeto integra um **Arduino UNO**, um **ESP-01** e um **sensor de temperatura NTC**, com exibição em **LCD I2C** e envio remoto de dados para um servidor Flask no **Render**, que armazena os valores no **Firebase Realtime Database** e exibe um **gráfico responsivo acessível via navegador**.

---

## ⚙️ Funcionalidades

- 📡 Envio de dados de temperatura via ESP-01 para um servidor online (Flask)
- 📊 Visualização gráfica em tempo real pelo navegador (com autoatualização)
- 📱 Layout responsivo para celular
- 💾 Armazenamento de dados no Firebase
- 🧊 Controle de ar-condicionado via relé com base em temperatura mínima/máxima
- 📟 Exibição da temperatura atual no LCD 16x2 (via I2C)

---

## 🔌 Esquema de ligação

| Componente         | Pino Arduino         | Observação                                 |
|--------------------|----------------------|--------------------------------------------|
| Sensor NTC         | A2                   | Com divisor resistivo                      |
| LCD I2C            | A4 (SDA), A5 (SCL)   | Alimentado via 5V/GND da protoboard        |
| ESP-01 (adaptador) | D2 (TX), D3 (RX)     | Comunicação serial com SoftwareSerial      |
| Relé (AC)          | D8                   | Aciona o ar-condicionado                   |
| Protoboard         | 5V / GND             | Alimenta LCD e ESP via trilhas positivas   |

---

## 🧪 Lógica de funcionamento

### No **Arduino UNO**:
- Lê a temperatura com um NTC
- Exibe no LCD 16x2 via I2C
- Controla o relé conforme:
  - Temperatura ≥ 26°C → **liga** o ar-condicionado
  - Temperatura ≤ 22°C → **desliga**
- Envia a temperatura via SoftwareSerial para o ESP-01

### No **ESP-01**:
- Conecta-se ao Wi-Fi
- Recebe dados via Serial do Arduino
- Envia os dados para o endpoint `/dados` de um servidor Flask hospedado no Render

### No **servidor Flask (Render)**:
- Rota `/dados?temp=XX.X` → grava os dados no Firebase
- Rota `/grafico` → exibe um gráfico interativo em tempo real com os dados

---

## 🌐 Endpoints do servidor

- `/dados?temp=XX.X` → recebe e grava temperatura
- `/grafico` → mostra o gráfico com autoatualização a cada 15 segundos

---

## 📦 Tecnologias utilizadas

- Arduino UNO + NTC + LCD I2C + ESP-01
- Flask (Render)
- Firebase Realtime Database
- Chart.js
- HTML + CSS responsivo

---

## 📲 Exemplo de acesso remoto

- **Gráfico em tempo real:**  
  [`https://projetoarduino.onrender.com/grafico`](https://projetoarduino.onrender.com/grafico)

- **Teste de envio:**  
  `https://projetoarduino.onrender.com/dados?temp=24.8`

---

## 🛠️ Para rodar localmente (servidor Flask)

```bash
pip install flask requests
python app.py
