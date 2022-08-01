#produtos = ['apple tv', 'mac', 'iphone x', 'iPad', 'apple watch', 'mac book', 'airpods']

#produtos.sort()
#print(produtos)

#produtos.sort(reverse = True)
#print(produtos)


def padronizar_codigos(lista_codigo, padrao='m'):
    for i, item in enumerate (lista_codigo):
       item = item.replace('  ',' ')
       item = item.strip()
       if padrao == 'm':
           item = item.casefold()
       elif padrao == 'M':
           item = item.upper()
       lista_codigo [i] = item
    return lista_codigo

cod_produtos = [' ABC12 ', 'abc34', 'AbC37']
print(padronizar_codigos(cod_produtos, padrao = 'm'))