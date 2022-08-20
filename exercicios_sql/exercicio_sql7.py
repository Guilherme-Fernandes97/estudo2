import pandas as pd
import sqlite3

conexao = sqlite3.connect('salarios.sqlite')
tabela_salarios = pd.read_sql('SELECT * FROM Salaries', conexao)
conexao.close()

import pyodbc

dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=salarios.sqlite")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

cursor.execute('SELECT * FROM Salaries')
valores = cursor.fetchall()
descricao = cursor.description

cursor.close()
conexao.close()

colunas = [tupla[0] for tupla in descricao]
tabela_salarios2 = pd.DataFrame.from_records(valores, columns=colunas)
tabela_salarios = tabela_salarios.loc[tabela_salarios["Agency"]=="San Francisco", :]

tabela_sm = tabela_salarios.groupby("Year").mean()

print(tabela_sm[['TotalPay', 'TotalPayBenefits']])

tabela_qtde = tabela_salarios.groupby("Year").count()
tabela_qtde = tabela_qtde[['Id']]
tabela_qtde = tabela_qtde.rename(columns={"Id": "Qtde"})
print(tabela_qtde)

def formatar(valor):
    return 'R${:,.2f}'.format(valor)

tabela_total = tabela_salarios.groupby("Year").sum()
tabela_total = tabela_total[['TotalPay', 'TotalPayBenefits']]
tabela_total['TotalPay'] = tabela_total['TotalPay'].apply(formatar)
tabela_total['TotalPayBenefits'] = tabela_total['TotalPayBenefits'].apply(formatar)
print(tabela_total)



