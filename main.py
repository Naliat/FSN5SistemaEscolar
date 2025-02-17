from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

DB_CONFIG = {
    "dbname": "SistemaEscola",
    "user": "postgres",
    "password": "lalalala",
    "host": "localhost",
    "port": "5432"
}

def get_db_connection():
    """Estabelece e retorna uma conexão com o banco de dados."""
    conn = psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
    return conn

@app.route('/')
def home():
    """
    Endpoint para testar a conexão com o banco de dados.
    Se a conexão for estabelecida com sucesso, retorna uma mensagem informando.
    """
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify({"message": "Conexão com o BD estabelecida com sucesso!"})
    except Exception as e:
        return jsonify({"message": "Falha na conexão com o BD.", "error": str(e)}), 500

### CRUD PARA PROFESSORES ###

@app.route('/professores', methods=['GET'])
def get_professores():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM professores;")
    professores = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(professores)

@app.route('/professores/<int:id>', methods=['GET'])
def get_professor(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM professores WHERE id = %s;", (id,))
    professor = cur.fetchone()
    cur.close()
    conn.close()
    if professor:
        return jsonify(professor)
    return jsonify({'message': 'Professor não encontrado'}), 404

@app.route('/professores', methods=['POST'])
def create_professor():
    data = request.get_json()
    nome = data.get('nome')
    departamento = data.get('departamento')
    if not nome or not departamento:
        return jsonify({'message': 'Nome e departamento são obrigatórios'}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO professores (nome, departamento) VALUES (%s, %s) RETURNING *;",
                (nome, departamento))
    novo_professor = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(novo_professor), 201

@app.route('/professores/<int:id>', methods=['PUT'])
def update_professor(id):
    data = request.get_json()
    nome = data.get('nome')
    departamento = data.get('departamento')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE professores SET nome = %s, departamento = %s WHERE id = %s RETURNING *;",
                (nome, departamento, id))
    professor_atualizado = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if professor_atualizado:
        return jsonify(professor_atualizado)
    return jsonify({'message': 'Professor não encontrado'}), 404

@app.route('/professores/<int:id>', methods=['DELETE'])
def delete_professor(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM professores WHERE id = %s RETURNING *;", (id,))
    professor_deletado = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if professor_deletado:
        return jsonify({'message': 'Professor deletado com sucesso'})
    return jsonify({'message': 'Professor não encontrado'}), 404

### CRUD PARA DISCIPLINAS ###

@app.route('/disciplinas', methods=['GET'])
def get_disciplinas():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM disciplinas;")
    disciplinas = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(disciplinas)

@app.route('/disciplinas/<int:id>', methods=['GET'])
def get_disciplina(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM disciplinas WHERE id = %s;", (id,))
    disciplina = cur.fetchone()
    cur.close()
    conn.close()
    if disciplina:
        return jsonify(disciplina)
    return jsonify({'message': 'Disciplina não encontrada'}), 404

@app.route('/disciplinas', methods=['POST'])
def create_disciplina():
    data = request.get_json()
    nome = data.get('nome')
    carga_horaria = data.get('carga_horaria')
    professor_id = data.get('professor_id')
    if not nome or not carga_horaria or not professor_id:
        return jsonify({'message': 'Nome, carga horária e professor_id são obrigatórios'}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO disciplinas (nome, carga_horaria, professor_id)
        VALUES (%s, %s, %s) RETURNING *;
    """, (nome, carga_horaria, professor_id))
    nova_disciplina = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(nova_disciplina), 201

@app.route('/disciplinas/<int:id>', methods=['PUT'])
def update_disciplina(id):
    data = request.get_json()
    nome = data.get('nome')
    carga_horaria = data.get('carga_horaria')
    professor_id = data.get('professor_id')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE disciplinas SET nome = %s, carga_horaria = %s, professor_id = %s
        WHERE id = %s RETURNING *;
    """, (nome, carga_horaria, professor_id, id))
    disciplina_atualizada = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if disciplina_atualizada:
        return jsonify(disciplina_atualizada)
    return jsonify({'message': 'Disciplina não encontrada'}), 404

@app.route('/disciplinas/<int:id>', methods=['DELETE'])
def delete_disciplina(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM disciplinas WHERE id = %s RETURNING *;", (id,))
    disciplina_deletada = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if disciplina_deletada:
        return jsonify({'message': 'Disciplina deletada com sucesso'})
    return jsonify({'message': 'Disciplina não encontrada'}), 404

### CRUD PARA ALUNOS ###

@app.route('/alunos', methods=['GET'])
def get_alunos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM alunos;")
    alunos = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(alunos)

@app.route('/alunos/<int:id>', methods=['GET'])
def get_aluno(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM alunos WHERE id = %s;", (id,))
    aluno = cur.fetchone()
    cur.close()
    conn.close()
    if aluno:
        return jsonify(aluno)
    return jsonify({'message': 'Aluno não encontrado'}), 404

@app.route('/alunos', methods=['POST'])
def create_aluno():
    data = request.get_json()
    nome = data.get('nome')
    data_nascimento = data.get('data_nascimento')  # Formato: 'YYYY-MM-DD'
    if not nome or not data_nascimento:
        return jsonify({'message': 'Nome e data_nascimento são obrigatórios'}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO alunos (nome, data_nascimento)
        VALUES (%s, %s) RETURNING *;
    """, (nome, data_nascimento))
    novo_aluno = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(novo_aluno), 201

@app.route('/alunos/<int:id>', methods=['PUT'])
def update_aluno(id):
    data = request.get_json()
    nome = data.get('nome')
    data_nascimento = data.get('data_nascimento')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE alunos SET nome = %s, data_nascimento = %s
        WHERE id = %s RETURNING *;
    """, (nome, data_nascimento, id))
    aluno_atualizado = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if aluno_atualizado:
        return jsonify(aluno_atualizado)
    return jsonify({'message': 'Aluno não encontrado'}), 404

@app.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM alunos WHERE id = %s RETURNING *;", (id,))
    aluno_deletado = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if aluno_deletado:
        return jsonify({'message': 'Aluno deletado com sucesso'})
    return jsonify({'message': 'Aluno não encontrado'}), 404

### CRUD PARA MATRÍCULAS ###

@app.route('/matriculas', methods=['GET'])
def get_matriculas():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM matriculas;")
    matriculas = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(matriculas)

@app.route('/matriculas/<int:id>', methods=['GET'])
def get_matricula(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM matriculas WHERE id = %s;", (id,))
    matricula = cur.fetchone()
    cur.close()
    conn.close()
    if matricula:
        return jsonify(matricula)
    return jsonify({'message': 'Matrícula não encontrada'}), 404

@app.route('/matriculas', methods=['POST'])
def create_matricula():
    data = request.get_json()
    aluno_id = data.get('aluno_id')
    disciplina_id = data.get('disciplina_id')
    data_matricula = data.get('data_matricula')  # Formato: 'YYYY-MM-DD'
    if not aluno_id or not disciplina_id or not data_matricula:
        return jsonify({'message': 'aluno_id, disciplina_id e data_matricula são obrigatórios'}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO matriculas (aluno_id, disciplina_id, data_matricula)
        VALUES (%s, %s, %s) RETURNING *;
    """, (aluno_id, disciplina_id, data_matricula))
    nova_matricula = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(nova_matricula), 201

@app.route('/matriculas/<int:id>', methods=['PUT'])
def update_matricula(id):
    data = request.get_json()
    aluno_id = data.get('aluno_id')
    disciplina_id = data.get('disciplina_id')
    data_matricula = data.get('data_matricula')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE matriculas SET aluno_id = %s, disciplina_id = %s, data_matricula = %s
        WHERE id = %s RETURNING *;
    """, (aluno_id, disciplina_id, data_matricula, id))
    matricula_atualizada = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if matricula_atualizada:
        return jsonify(matricula_atualizada)
    return jsonify({'message': 'Matrícula não encontrada'}), 404

@app.route('/matriculas/<int:id>', methods=['DELETE'])
def delete_matricula(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM matriculas WHERE id = %s RETURNING *;", (id,))
    matricula_deletada = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if matricula_deletada:
        return jsonify({'message': 'Matrícula deletada com sucesso'})
    return jsonify({'message': 'Matrícula não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
