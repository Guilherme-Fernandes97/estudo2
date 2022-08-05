meta = 10000
vendas = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 3750,
    'Ana': 10300,
    'Alon': 7870,
}

def calculo_meta(meta, vendas):
    meta_batida = []
    for vendedor in vendas:
        if vendas[vendedor] >= meta:
            meta_batida.append(vendedor)
            percen_bateu_meta = len(meta_batida) / len(vendas)
    return percen_bateu_meta, meta_batida


p_meta, vendedores_acima_meta = calculo_meta(meta, vendas)
print(f'{p_meta:.1%}')
print(vendedores_acima_meta)