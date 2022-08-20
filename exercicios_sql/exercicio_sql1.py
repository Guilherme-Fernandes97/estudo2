import pyodbc

dados_conexao = ('Driver={SQLite3 ODBC Driver};'
           'Server=localhost;'
           'Database=salarios.sqlite')

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute("SELECT * FROM Salaries")
valores = cursor.fetchall()

cursor.close()
conexao.close()