vendas = [
    ['maçã', 5],
    ['banana', 15],
    ['azeite', 1],
    ['vinho', 3],
]

vendas = []

while True:
    produto = input('Qual o produto ?')
    if not produto:
        break
    qtde = int(input('qual a quantidade ?'))
    vendas.append([produto, qtde])
print(vendas)