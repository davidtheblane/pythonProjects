from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = [
    {
        "id": 1,
        "descricao": "Estudar Python e Flask",
        "concluida": True
    },
    {
        "id": 2,
        "descricao": "Criar minha primeira API",
        "concluida": False
    }
]

carro = {
    "marca": "Fiat",
    "modelo": "Uno",
    "ano": "2025"
}


@app.route('/')
def home():
    return 'Bem Vindo a minha primeira API!'


@app.route('/carro', methods=['GET'])
def get_carro():
    return jsonify(carro)


@app.route('/tarefas', methods=['GET'])
def get_tarefas():
    return jsonify(tarefas)


@app.route('/tarefas', methods=['POST'])
def add_tarefa():
    nova_tarefa = request.json
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201


if __name__ == '__main__':
    app.run(debug=True)
