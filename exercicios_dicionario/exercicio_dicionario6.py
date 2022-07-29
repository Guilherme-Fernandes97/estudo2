produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus']
vendas = [15000, 12000, 10000, 14300, 1720, 1000, 2500, 1000, 17000, 2450]

#transformando lista em tupla
lista_tuplas = zip(produtos, vendas)
print(lista_tuplas)
print('-' * 40)

#transformando tupla em dicionario
dicionario_vendas = dict(lista_tuplas)
print(dicionario_vendas)
print('-' * 40)

#Quanto vendemos de ipad ? por lista
indice = produtos.index('ipad')
print(f'Vendemos {vendas[indice]} ipads')

#por dicionario
print(f'Vendemos {dicionario_vendas["ipad"]} ipads')

