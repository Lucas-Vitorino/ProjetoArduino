from flask import Flask, request
import requests
import datetime

app = Flask(__name__)

# 🔥 Substitua abaixo pelas suas credenciais reais do Firebase:
FIREBASE_URL = "https://temp-arduino-9c80f-default-rtdb.firebaseio.com/"
FIREBASE_SECRET = "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCHWJ7CAxzBAcco\nrTPkmPaPaxwTttDtmnJ+A/rHmtuFwYlaSUQ4y5EB3hpSqiyJa0rc6fuaX97GJqva\nPalq/OJ+dffzA90UwFBeXKZ+CBUsHaR8dWmJCyOY/xFLE0djg9C6ckDxfS+ueLpc\nRa7+UbgWk0dyx5cXnTJPW4Qe6WDkZi3YHFiMJJTriK6dGmyfm5TmIOjWIp/5WS/n\nROcNAKoOji7emYLqkjvnYXY+qnVtwTbrdRhMq5uoGr6o1z+1+GMfqNLJaPkKNHDL\n7uU/xPATXwgyeKJ5CJ6yfz+DG0GV9S2XSvnaTJqnKgRxYV6hk/IXgBdKmQdlRn/n\n0NT2A/JZAgMBAAECggEAAVrEMzBHyRcekKXAt4Cszj0/fMnSgayovHuHg37lXb6h\nnfs0vEkuEtg2G25J+Tgb+cw65E3uub0ovb7qcEBgRFOKHzvPKlMaATYpKzXwGRuh\no7M8uQ5MLwHo50wlzA7e950g6qnN+kK824nA/7LLeY8qYsr9+p9sO2B9mOrNOVi+\nuJQRcxuwcSJbM9erA0dOzUnWihOlWu05b2IhfCKMVZDOyWK7+z7jOecaYMQoOIuN\nKIUp6Ay3qC7w+l1YVDb/oFr7Vwwgov4zcOmHFM2QhwAacPlaE4o/QG4OBcooVbGH\nkscXEQnQiRJ7zAGphmu/G56bezdXkpxedMJy2A8lAQKBgQC87RxKE1fRqOeonDzt\nenv+v3kdLTWBt/E07uc/oWs5rQpOJ2zJI4EgCzKaSAz4ayzumim1exdW21Zhit2i\nYSBJ0JIdHkW12xqzevvbdTucLbhZ3oN4tHb7oAnetVHiVxw+MMu5ijT1BJ2KgSy7\nCanm18FfxJrSV9A9jL0vHDErQQKBgQC3Zcs8z2ScOIVWLBVT15ngT2M1WSdqxAJ6\nNMJTXL1DD7Dv+pxngmyvXAj34cxeaM99fOv8R97uYurc3G8jLp9pJNrMw1lnW2yg\nbboYdGDrYzMih7bt3ARZtDybhvRLv9tKOJyVszyedWIZ93EzqTc8FtXSj+/FNcOX\nWktXv4V5GQKBgQCkZCXThxVJSBGbs6eIdKXkOzPl4WrHnwjxqFfsFEc6/okTDFcq\nhgxbl6LGgJ9YodmNHPPiCGN8noqBgdXs71qrICOj1q2N2kNXnVH92fquoVHiUS5R\nH6bQuKcd9OR1cJsQumDq54nBEe0Lke8cKQJ/7YlEDc0x7lsy033iukNGgQKBgFDF\nDRgwApBmuBp2ecIeHw/SBtBU/m4f+zNVDwxluJjTTUqzZbSUlUc50l1RXY9qu475\nuHi4Mm9ssyEoF+43t084QwCRPEuv0Qxqpt3kS1b/rmKTwLXLA0N6hIK+kdLWoT5z\n5kpr0NO8wMLM3lcxPDlDmVINwDxrbEO5KZtwptjpAoGAVTDjyALAxy9NGMu9O44n\nhgG52gvBdF6MDX1rINYDEJXtK4NZklwrI/SsBf7Mv+1BW3P8Y6BaoNbYafFumgcA\nCWLLC8Mc4hzhhr+7f4ooK5eWdozwF9dWoBrHbtGTpf0HI9v/4HWxo3BC602lEkDX\nSvBgGmCf1ok1TKP0uAxTZog=\n-----END PRIVATE KEY-----\n"

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
    app.run()
