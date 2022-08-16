preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000, 'ps5': 3000, 'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}

def calcular_preco(preco):
    return preco * 1.3

preco_com_imposto = list(map(calcular_preco, preco_tecnologia.values()))
print(preco_com_imposto)

#Com lambda

preco_com_imposto2 = list(map(lambda preco: preco * 1.3, preco_tecnologia.values()))
print(preco_com_imposto2)

#fazendo por function
def ehmaior2000(item):
    return item[1] > 2000

produtos_acima2000 = dict(list(filter(ehmaior2000, preco_tecnologia.items())))
print(produtos_acima2000)

#fazendo por lambda
produtos2_acima2000 = dict(list(filter(lambda item: item[1] > 2000 , preco_tecnologia.items())))
print(produtos2_acima2000)