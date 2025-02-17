CREATE TABLE IF NOT EXISTS professores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    departamento VARCHAR(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS disciplinas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    carga_horaria INTEGER NOT NULL,
    professor_id INTEGER NOT NULL,
    FOREIGN KEY (professor_id) REFERENCES professores (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS matriculas (
    id SERIAL PRIMARY KEY,
    aluno_id INTEGER NOT NULL,
    disciplina_id INTEGER NOT NULL,
    data_matricula DATE NOT NULL,
    FOREIGN KEY (aluno_id) REFERENCES alunos (id) ON DELETE CASCADE,
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas (id) ON DELETE CASCADE
);

INSERT INTO professores (nome, departamento) VALUES 
('João Silva', 'Matemática'),
('Maria Oliveira', 'História'),
('Pedro Souza', 'Física'),
('Ana Costa', 'Química'),
('Carla Martins', 'Biologia'),
('Luis Mendes', 'Português'),
('Paula Ramos', 'Geografia'),
('Marcos Lima', 'Artes'),
('Fernanda Dias', 'Educação Física'),
('Roberto Nunes', 'Filosofia');


INSERT INTO disciplinas (nome, carga_horaria, professor_id) VALUES 
('Álgebra', 60, 1),
('Geometria', 60, 1),
('História Mundial', 45, 2),
('Física I', 60, 3),
('Química Orgânica', 50, 4),
('Biologia Geral', 55, 5),
('Gramática', 40, 6),
('Geografia do Brasil', 45, 7),
('História da Arte', 35, 8),
('Filosofia Moderna', 50, 10);

INSERT INTO alunos (nome, data_nascimento) VALUES 
('Carlos Souza', '2005-05-12'),
('Ana Pereira', '2006-08-22'),
('Ricardo Alves', '2005-09-15'),
('Mariana Gomes', '2006-03-08'),
('Felipe Silva', '2005-12-30'),
('Patricia Lima', '2006-07-21'),
('Eduardo Santos', '2005-11-02'),
('Bruna Castro', '2006-01-17'),
('Gustavo Pires', '2005-04-25'),
('Sofia Rodrigues', '2006-10-10');


INSERT INTO matriculas (aluno_id, disciplina_id, data_matricula) VALUES 
(1, 1, '2025-01-10'),
(1, 3, '2025-01-11'),
(2, 2, '2025-01-12'),
(2, 4, '2025-01-13'),
(3, 5, '2025-01-14'),
(4, 6, '2025-01-15'),
(5, 7, '2025-01-16'),
(6, 8, '2025-01-17'),
(7, 9, '2025-01-18'),
(8, 10, '2025-01-19');


SELECT * FROM professores;

SELECT * FROM disciplinas;

SELECT * FROM alunos;

SELECT * FROM matriculas;


