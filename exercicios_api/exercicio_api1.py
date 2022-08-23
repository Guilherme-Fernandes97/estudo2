import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
cotacoes_dic = cotacoes.json()


#print(f'Dólar valor: {cotacoes_dic["USD"]["bid"]}')
#print(f'Euro valor: {cotacoes_dic["EUR"]["bid"]}')
#print(f'Bitcoin valor: {cotacoes_dic["BTC"]["bid"]}')

cotacoes_30dias = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
cotacoes_dic30 = cotacoes_30dias.json()

#print(f'{cotacoes_dic30[0]}')

lista_cotacoes_Dolar = [float(item['bid']) for item in cotacoes_dic30]
print(lista_cotacoes_Dolar)
