def cadastrar_produto():
    produto = input('Digite o nome do produto que deseja cadastrar')
    produto = produto.casefold()
    print(f'produto {produto} cadastrado com sucesso')

for i in range(3):
    cadastrar_produto()
