produtos = ['apple tv', 'mac', 'IPhone x', 'IPhone 11', 'IPad', 'apple watch', 'mac book', 'airpods']

produtos.sort(key=str.casefold)
print(produtos)

vendas_produtos = {'vinho': 100, 'cafeiteira': 150, 'microondas': 300, 'iphone': 5500}

def segundo_item(tupla):
    return tupla[1]
lista_vendas = list(vendas_produtos.items())
lista_vendas.sort(key=segundo_item, reverse=True)
print(dict(lista_vendas))