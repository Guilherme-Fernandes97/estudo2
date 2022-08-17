arquivo = open('Alunos.txt', 'r')
linhas = arquivo.readlines()
del linhas[:4]

qtde_anuncio = 0
qtde_org = 0
qtde_yt_org = 0
qtde_igfb_org = 0
qtde_site_org = 0

for linha in linhas:
    email, origem = linha.split(',')
    if '_org' in origem:
        qtde_org += 1
        if '_yt_org' in origem:
            qtde_yt_org += 1
        if '_site_org' in origem:
            qtde_site_org += 1
        if '_ig_org' in origem or '_igfb_org' in origem:
            qtde_igfb_org += 1
    else:
        qtde_anuncio += 1

qtde_total = qtde_org + qtde_anuncio

arquivo.close()

with open('Indicadores.txt', 'w') as arquivo_indicadores:
    arquivo_indicadores.write(f'Quantidade anuncio: {qtde_anuncio}\n')
    arquivo_indicadores.write(f'Quantidade organico:{qtde_org}\n')
    arquivo_indicadores.write(f'Quantidade instagram:{qtde_igfb_org}\n')
    arquivo_indicadores.write(f'Quantidade youtube:{qtde_yt_org}\n')
    arquivo_indicadores.write(f'Quantidade site:{qtde_site_org}\n')
    arquivo_indicadores.write(f'Quantidade total de alunos {qtde_total}\n')