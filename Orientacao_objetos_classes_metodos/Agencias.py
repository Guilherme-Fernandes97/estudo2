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


class AgenciaComum(Agencia):

    pass

class AgenciaPremium(Agencia):

    pass



agencia1 = Agencia(22222, 3289320, 30902)

agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br', 2002200, 200202)
agencia_virtual.verificar_caixa()
print(agencia_virtual.telefone)