import sqlite3

#Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE Estudantes")

#Cria tabela Estudantes com os campos: ID(chave primária); Nome; Curso; Ano de Ingresso
cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudantes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    AnoIngresso INTEGER
);
""")

#Adiciona as informações dos estudantes
alunos = [
    ('Ana Silva', 'Computação', 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alves', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022)
]

#Insere diversos registros de uma vez no banco de dados
cursor.executemany("""
INSERT INTO Estudantes (Nome, Curso, AnoIngresso)
VALUES (?, ?, ?);
""", alunos)

#Confirma alterações usando o método commit() do objeto de conexão
conn.commit()

#Mostra tabela original
cursor.execute("SELECT * FROM Estudantes")
print(cursor.fetchall())

#Mostra tabela com alunos que ingressaram somente em 2019 ou 2020
cursor.execute("SELECT * FROM Estudantes WHERE AnoIngresso=2019 OR AnoIngresso=2020")
print(cursor.fetchall())

#Realiza o update do ano de ingresso de um dos alunos
cursor.execute("UPDATE Estudantes SET AnoIngresso=2020 WHERE Nome='João Alves'")
conn.commit()

#Deleta um estudante da tabela
cursor.execute("DELETE FROM Estudantes WHERE ID=1 ")
conn.commit()

#Seleciona e mostra os alunos em que o ano de ingresso é após 2019
cursor.execute("SELECT * FROM Estudantes WHERE AnoIngresso>2019 AND Curso='Computação'")
print(cursor.fetchall())

#Realiza o update de todos os alunos para o ano de ingresso 2020
cursor.execute("UPDATE Estudantes SET AnoIngresso=2018 WHERE Curso='Computação'")
conn.commit()

cursor.execute("SELECT * FROM Estudantes")
print(cursor.fetchall())


conn.close()

