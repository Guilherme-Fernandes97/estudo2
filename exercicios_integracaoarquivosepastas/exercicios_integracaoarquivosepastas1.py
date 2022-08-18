from pathlib import Path
import shutil

caminho = Path('Arquivos_Lojas')
arquivos = caminho.iterdir()

for arquivo in arquivos:
    print(arquivo)

if (caminho / Path('202004_Shopping Tijuca_RJ.csv')).exists():
    print('Existe')

#criar pasta
#Path('Pasta auxiliar/Pasta 2').mkdir()

arquivo_copiar = Path('Arquivos_Lojas/202004_Shopping Cidade_MG.csv')
arquivo_colar = Path('Pasta auxiliar/Pasta 2/202004_Shopping Cidade_MG_versao2.csv')
shutil.copy2(arquivo_copiar, arquivo_colar)


shutil.move(Path('Pasta auxiliar/Pasta 2/202004_Shopping Cidade_MG_versao2.csv'), Path('Pasta auxiliar/202004_Shopping Cidade_MG_versao2.csv'))