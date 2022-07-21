vendas = [102, 150, 1500, 2000, 120]
meta = 110

for venda in vendas:
    if venda < meta:
        print('A loja não ganha bônus')
        break

meta = 130
vendedores = ['João', 'Julia', 'Ana', 'José', 'Maria']

for venda in vendas:
    if venda < meta:
        continue
    print(venda)