from random import randint


class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nível recomendado. Caixa atual: R${self.caixa:,.2f}')
        else:
            print(f'O valor de caixa está ok. Caixa Atual: R${self.caixa:,.2f}')

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimo não é possível. Dinheiro não disponível em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self,valor):
        if self.caixa > valor:
            self.caixa -= valor
            self.caixa_paypal += valor
        else:
            print(f'Dinheiro não disponível em caixa, o caixa é de {self.caixa:,.2f}')

    def sacar_paypal(self, valor):
        if self.caixa > valor:
            self.caixa_paypal -= valor
            self.caixa += valor
        else:
            print(f'Dinheiro não disponível em caixa, o caixa é de {self.caixa_paypal:,.2f}')

class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000


class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print(f'O cliente não tem o patrimônio mínimo necessário para entrar na âgencia premium')


agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br', 1023032, 1032032 )
agencia_virtual.depositar_paypal(900000)

print(agencia_virtual.caixa_paypal)

agencia_virtual.sacar_paypal(800000)

print(agencia_virtual.caixa_paypal)
print(agencia_virtual.caixa)

print('-' * 90)

agencia_premium = AgenciaPremium(1031020, 13902392,)
agencia_premium.adicionar_cliente('Guilherme', 132032, 8000000)
print(agencia_premium.clientes)