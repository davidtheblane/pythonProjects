import os
import psycopg2.extras
from dotenv import load_dotenv
from flask import Flask, jsonify, request

load_dotenv()
app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD')
    )
    return conn


@app.route('/')
def home():
    return 'Bem Vindo a API de Tarefas com PostgreSQL!'


@app.route('/tarefas', methods=['GET'])
def get_tarefas():
    conn = get_db_connection()
    # psycopg2.cursors.DictCursor faz com que o resultado da busca venha como um dicionário
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Executa o comando SQL
    cur.execute('SELECT * FROM tarefas ORDER BY id ASC;')

    # Busca todos os resultados
    tarefas = cur.fetchall()

    # Fecha o cursor e a conexão
    cur.close()
    conn.close()

    # O resultado de 'fetchall' já é uma lista de "dicionários",
    # então podemos passá-la diretamente para o jsonify.
    return jsonify(tarefas)


@app.route('/tarefas', methods=['POST'])
def add_tarefa():
    nova_tarefa_data = request.json

    # Validação simples para garantir que a 'descricao' foi enviada
    if not nova_tarefa_data or 'descricao' not in nova_tarefa_data:
        return jsonify({"erro": "A descrição da tarefa é obrigatória"}), 400

    descricao = nova_tarefa_data['descricao']

    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute('INSERT INTO tarefas (descricao) VALUES (%s) RETURNING *;',
                    (descricao,))

        tarefa_criada = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()

        return jsonify(tarefa_criada), 201

    except psycopg2.OperationalError as e:
        # Erro de conexão com o banco
        return jsonify({"erro": "Não foi possível conectar ao banco de dados"}), 500
    except Exception as e:
        # Captura outros erros inesperados
        return jsonify({"erro": f"Um erro inesperado ocorreu: {e}"}), 500


@app.route('/tarefas/<int:id>', methods=['PUT'])
def update_tarefa(id):
    dados_tarefa = request.json
    concluida = dados_tarefa.get('concluida')

    if concluida is None or not isinstance(concluida, bool):
        return jsonify({"erro": "O campo 'concluida' é obrigatório e deve ser um booleano (true/false)"}), 400

    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # Executa o UPDATE, focando apenas no campo 'concluida'
        cur.execute('UPDATE tarefas SET concluida = %s WHERE id = %s RETURNING *;',
                    (concluida, id))

        tarefa_atualizada = cur.fetchone()

        # Se a tarefa não for encontrada, fetchone() retornará None
        if tarefa_atualizada is None:
            return jsonify({"erro": "Tarefa não encontrada"}), 404

        conn.commit()
        cur.close()
        conn.close()

        return jsonify(tarefa_atualizada)

    except Exception as e:
        return jsonify({"erro": f"Um erro inesperado ocorreu: {e}"}), 500


@app.route('/tarefas/<int:id>', methods=['DELETE'])
def delete_tarefa(id):

    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute('DELETE FROM tarefas WHERE id = %s RETURNING *;', (id,))

        tarefa_deletada = cur.fetchone()

        # Se a tarefa não for encontrada, fetchone() retornará None
        if tarefa_deletada is None:
            return jsonify({"erro": "Tarefa não encontrada"}), 404

        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"message": 'Tarefa removida com sucesso!'}), 200

    except Exception as e:
        return jsonify({"erro": f"Um erro inesperado ocorreu: {e}"}), 500


if __name__ == '__main__':
    # Usamos os.getenv para pegar a porta do .env ou usar 5000 como padrão
    api_port = 5000
    app.run(debug=True, port=api_port)
