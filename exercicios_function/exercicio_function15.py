produtos = [' ABC12 ', 'abc34', 'AbC37', 'beb12', ' BSA151', 'BEB23']

def padronizar_texto(texto):
    texto = texto.casefold()
    texto = texto.replace("  ", " ")
    texto = texto.strip()
    return texto

produtos = list(map(padronizar_texto, produtos))
print(produtos)
