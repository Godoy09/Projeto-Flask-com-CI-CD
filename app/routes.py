from flask import request, jsonify
from app import app

@app.route('/')
def home():
    return "API de Soma organizada!"

@app.route('/soma')
def soma():
    try:
        a = int(request.args.get('a', 0))
        b = int(request.args.get('b', 0))
        return jsonify({'resultado': a + b})
    except ValueError:
        return jsonify({'erro': 'Parâmetros inválidos'}), 400
