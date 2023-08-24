from db.db_utils import *
import sqlite3

#Impede o banco de dados de se repetir diversas vezes
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE Estudantes")

#Infos essenciais da tabela
nome_tabela = 'Estudantes'
campos ="(ID INTEGER PRIMARY KEY AUTOINCREMENT, Nome TEXT NOT NULL, Curso TEXT NOT NULL, AnoIngresso INTEGER)"
alunos = [
    ('Ana Silva', 'Computação', 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alves', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022)]

tabela = cria_tabela(nome_tabela, campos, alunos)

#Filtra alunos que ingressaram entre 2019 e 2020
tabela_2019_2020 = filtra(nome_tabela, 'AnoIngresso', 2019, 2020)

#Altera o ano de ingresso de um dos alunos
tabela_atualiza_anoingresso = update(nome_tabela, 'AnoIngresso', 2020, 'Nome', 'João Alves')

#Deleta um dos alunos do banco de dados
tabela_deleta1 = delete(nome_tabela, 'ID', 1)

#Seleciona e mostra os alunos em que o ano de ingresso é após 2019
tabela_pos2019_comp = filtra_ano_curso(nome_tabela, 'AnoIngresso', 2019, 'Curso', 'Computação')

#Concerta ano de ingresso dos alunos de computação para 2018
tabela_concerta_ano = update(nome_tabela, 'AnoIngresso', 2018, 'Curso', 'Computação')






