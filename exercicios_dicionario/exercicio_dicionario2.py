lucro_1tri = {'janeiro': 100000, 'fevereiro': 120000, 'março': 90000}
lucro_2tri = {'abril': 88000, 'maio': 89000, 'junho': 120000}
#adicionando 1 item
print(lucro_1tri)
#lucro_1tri['abril'] = 88000
#print(lucro_1tri)
#adicionando vários itens ou um dicionário a outro
lucro_1tri.update(lucro_2tri)
print(lucro_1tri)
#adicionando um item já existente (manualmente ou pelo update)
lucro_1tri['janeiro'] = 88000
print(lucro_1tri)

lucro_fev = 85000
lucro_1tri['fevereiro'] = lucro_fev
print(lucro_1tri)