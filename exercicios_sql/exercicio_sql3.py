import pyodbc
import pandas as pd

dados_conexao = ('Driver={SQLite3 ODBC Driver};'
           'Server=localhost;'
           'Database=chinook.db')

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute('SELECT * FROM customers')

valores = cursor.fetchall()
descricao = cursor.description
colunas = [tupla[0] for tupla in descricao]
tabela_clientes = pd.DataFrame.from_records(valores, columns=colunas)


print(tabela_clientes)


cursor.close()
conexao.close()
