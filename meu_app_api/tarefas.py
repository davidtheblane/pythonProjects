from flask import Flask, jsonify, request

ARQUIVO_TAREFAS = 'tarefas.txt'


def carregar_tarefas():
    try:
        with open(ARQUIVO_TAREFAS, 'r') as arquivo:
            tarefas = [linha.strip() for linha in arquivo]
            print(f"tarefas: {tarefas}")
            tarefas_dict = []
            for i, desc in enumerate(tarefas):
                tarefas_dict.append({
                    "id": i+1,
                    "descricao": desc,
                    "concluida": False
                })
        return tarefas_dict
    except FileNotFoundError:
        return []


def salvar_tarefas(lista_de_tarefas):
    with open(ARQUIVO_TAREFAS, 'w') as arquivo:
        for tarefa in lista_de_tarefas:
            arquivo.write(f"{tarefa["descricao"]}\n")


app = Flask(__name__)


@app.route('/')
def home():
    return 'Bem Vindo a lista de tarefas!'


@app.route('/tarefas', methods=['GET'])
def get_tarefas():
    tarefas = carregar_tarefas()
    return jsonify(tarefas)


@app.route('/tarefas', methods=['POST'])
def add_tarefa():
    tarefas = carregar_tarefas()

    nova_tarefa_data = request.json

    novo_id = len(tarefas) + 1

    nova_tarefa = {
        "id": novo_id,
        "descricao": nova_tarefa_data['descricao'],
        "concluida": False
    }

    tarefas.append(nova_tarefa)

    salvar_tarefas(tarefas)

    return jsonify(nova_tarefa), 201


if __name__ == '__main__':
    app.run(debug=True)
