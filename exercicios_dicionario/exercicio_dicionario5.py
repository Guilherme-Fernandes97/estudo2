vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000}

for chave in vendas_tecnologia:
    if vendas_tecnologia[chave] > 5000:
        print(f'{chave}: {vendas_tecnologia[chave]}')

print('--------')

for produto, qtde in vendas_tecnologia.items():
    if qtde > 5000:
        print(f'{produto}: {qtde}')

