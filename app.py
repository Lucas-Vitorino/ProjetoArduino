from flask import Flask, request, render_template, jsonify
import requests
import datetime

app = Flask(__name__)

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

@app.route('/api/dados')
def api_dados():
    r = requests.get(f"{FIREBASE_URL}/leituras.json?auth={FIREBASE_SECRET}")
    if r.status_code == 200:
        return jsonify(r.json())
    return jsonify({"erro": "Falha ao buscar dados"}), 500

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/api/ultima')
def ultima_temp():
    r = requests.get(f"{FIREBASE_URL}/leituras.json?auth={FIREBASE_SECRET}")
    if r.status_code == 200:
        dados = r.json()
        if dados:
            ultima = list(dados.values())[-1]
            temp = ultima.get("temperatura")
            hora_iso = ultima.get("hora")
            if temp and hora_iso:
                hora_utc = datetime.datetime.fromisoformat(hora_iso)
                hora_brt = hora_utc - datetime.timedelta(hours=3)
                return {
                    "temperatura": temp,
                    "data": hora_brt.strftime("%d/%m/%Y"),
                    "hora": hora_brt.strftime("%H:%M:%S")
                }
    return {"erro": "Sem dados"}, 404

@app.route('/grafico')
def grafico():
    return render_template("grafico.html")

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
