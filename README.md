# Regulador de Temperatura com Arduino

Este projeto utiliza um sensor de temperatura e um módulo relé para controlar automaticamente um sistema de ar-condicionado ou ventilação, com visualização em um display LCD.

## ⚙️ Componentes utilizados

- Arduino UNO
- Sensor de temperatura (NTC ou similar com a biblioteca `Thermistor`)
- Display LCD 16x2 (interface paralela)
- Módulo Relé
- Jumpers e Protoboard
- Fonte de alimentação externa (se necessário)

## 🧠 Funcionamento

O sistema lê a temperatura ambiente continuamente e age conforme os seguintes critérios:

- Se a temperatura **ultrapassar o valor máximo (ex: 29°C)**, o relé é **ativado**, ligando o sistema de refrigeração.
- Se a temperatura **cair abaixo do valor mínimo (ex: 20°C)**, o relé é **desligado**.
- A temperatura atual é exibida no display LCD em tempo real.

O projeto também conta com **histerese** para evitar ligações/desligações frequentes.

## 🛠️ Código

O código está disponível no arquivo `.ino` deste repositório. Você pode abri-lo diretamente na IDE do Arduino.

## 📦 Como usar

1. Conecte os componentes ao Arduino conforme o esquema do código.
2. Faça o upload do arquivo `.ino` via Arduino IDE.
3. Alimente o Arduino e observe a leitura e o controle automático da temperatura.

---

Sinta-se à vontade para personalizar os valores de temperatura mínima e máxima dentro do código.

## 📌 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
