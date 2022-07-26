mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}



print(f"O livro mais vendido foi {mais_vendidos['livros']}")
print(f"O livro mais vendido foi {mais_vendidos['lazer']}")

print(f'Vendemos {vendas_tecnologia.get("ipad")} ipads')
print(f'Vendemos {vendas_tecnologia.get("notebook asus")} notebooks')

if vendas_tecnologia.get('copo') == None:
    print('copo não esta dentro da lista de tecnologia')
else:
    print(vendas_tecnologia.get('copo'))