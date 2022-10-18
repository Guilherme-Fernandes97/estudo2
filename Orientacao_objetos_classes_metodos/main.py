from ContasBancos import ContaCorrente, CartaoCredito

conta_Lira = ContaCorrente("Lira", "111.222.333-45", 1234, 34062)

cartao_lira = CartaoCredito('Lira', conta_Lira)

print(cartao_lira.conta_corrente.num_conta)

print(cartao_lira.numero)
print(cartao_lira.cod_seguranca)
print(cartao_lira.validade)

cartao_lira.senha = '2345'
print(cartao_lira.senha)

print(conta_Lira.__dict__)