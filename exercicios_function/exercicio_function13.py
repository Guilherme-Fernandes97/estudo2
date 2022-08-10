def minha_soma(*numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma

print(minha_soma(10, 20, 30, 40))

def preco_final(preco, **adicionais):
    #print(adicionais)
    if 'desconto' in adicionais:
        preco *= (1 - adicionais['desconto'])
    if 'garantia_extra' in adicionais:
        preco += adicionais['garantia_extra']
    if 'imposto' in adicionais:
        preco *= (1 + adicionais['imposto'])
    return preco

print(preco_final(1000, desconto=0.1, garantia_extra=100))