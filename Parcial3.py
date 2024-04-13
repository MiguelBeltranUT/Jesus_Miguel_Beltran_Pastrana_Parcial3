from flask import Flask, request, jsonify
import pywhatkit

app = Flask(__name__)

tasks = [
    {"mensaje": "Hola, Soy miguel desde", "telefono": 4442201272}
]

@app.route('/tasks', methods=['GET'])
def get_task():
        pywhatkit.sendwhatmsg_instantly("+5215569656239", "Hola")
        return jsonify(task)

if __name__ == '__main__':
    app.run(debug=True)
