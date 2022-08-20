import pyodbc

dados_conexao = ('Driver={SQLite3 ODBC Driver};'
           'Server=localhost;'
           'Database=chinook.db')

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute("""
INSERT INTO albums (Title, ArtistId)
VALUES
('Lira Rock', 4)
""")

cursor.commit()










cursor.close()
conexao.close()
