import pyodbc

dados_conexao = ('Driver={SQLite3 ODBC Driver};'
           'Server=localhost;'
           'Database=chinook.db')
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute('''
UPDATE customers SET Email="lira@embraer.com.br" WHERE Email="luisg@embraer.com.br"
''')

cursor.commit()


cursor.close()
conexao.close()