from flask import Flask, request, render_template
import requests
import datetime

app = Flask(__name__)

# Configurações do Firebase
FIREBASE_URL = "https://temp-arduino-9c80f-default-rtdb.firebaseio.com"
FIREBASE_SECRET = "702d5600320cddab9dc1af8ab50e0da4a2f09047"

@app.route('/dados', methods=['GET'])
def receber_dados():
    temp = request.args.get('temp')

    if temp:
        agora = datetime.datetime.now().isoformat()
        dado = {
            "temperatura": float(temp),
            "hora": agora
        }

        r = requests.post(f"{FIREBASE_URL}/leituras.json?auth={FIREBASE_SECRET}", json=dado)

        if r.status_code == 200:
            return f"OK - Temperatura {temp} registrada."
        else:
            return f"Erro ao enviar ao Firebase: {r.text}", 500

    return "Parâmetro 'temp' ausente", 400

@app.route('/')
def home():
    return 'Servidor do Arduino está online!'

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

# Adicionando a rota para o gráfico


@app.route('/grafico')
def grafico():
    return render_template("grafico.html")


