import sqlite3

#Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

def cria_tabela(nome_tabela, campos_tabela, dados_tabela):
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {nome_tabela} {campos_tabela};')
    conn.commit()

    cursor.executemany(f'INSERT INTO {nome_tabela} (Nome, Curso, AnoIngresso) VALUES (?, ?, ?);', dados_tabela)
    conn.commit()

    cursor.execute(f'SELECT * FROM {nome_tabela}')
    print(cursor.fetchall())


def filtra(nome_tabela, campo, restricao1, restricao2):
    cursor.execute(f'SELECT * FROM {nome_tabela} WHERE {campo}={restricao1} OR {campo}={restricao2}')
    print(cursor.fetchall())


def update(nome_tabela, campo_set, restricao_set, campo_where, restricao_where):

    query = f'UPDATE {nome_tabela} SET {campo_set}=? WHERE {campo_where}=?'

    cursor.execute(query, (restricao_set, restricao_where))
    conn.commit()

    cursor.execute(f'SELECT * FROM {nome_tabela}')
    print(cursor.fetchall())


def delete(nome_tabela, campo, restricao):
    cursor.execute(f'DELETE FROM {nome_tabela} WHERE {campo}={restricao}')
    conn.commit()

    cursor.execute(f'SELECT * FROM {nome_tabela}')
    print(cursor.fetchall())


def filtra_ano_curso(nome_tabela, campo1, campo2, restricao1, restricao2):
    query = f'SELECT * FROM {nome_tabela} WHERE {campo1} > ? AND {campo2} = ?'
    cursor.execute(query, (restricao1, restricao2))
    
    result = cursor.fetchall()
    for row in result:
        print(row)



