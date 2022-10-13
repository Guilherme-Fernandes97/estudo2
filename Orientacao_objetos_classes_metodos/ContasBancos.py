class ContaCorrente:

    def __init__(self, nome, cpf):
        self.limite = None
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def consultar_saldo(self):
        print(f'Seu saldo atual é de R${self.saldo:,.2f}')

    def depositar(self, valor):
        self.saldo =+ valor

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor.')
            self.consultar_saldo()
        else:
            self.saldo -= valor

    def consultar_limite_chequeespecial(self):
        print(f'Seu limite de Cheque Especial é de R${self._limite_conta():,.2f}')


# Programa

conta_Lira = ContaCorrente("Lira", "111.222.333-45")
conta_Lira.consultar_saldo()

# Depositando dinheiro na conta
conta_Lira.depositar(10000)
conta_Lira.consultar_saldo()

# Sacando dinheiro da conta
conta_Lira.sacar_dinheiro(10000)

conta_Lira.consultar_saldo()
conta_Lira.consultar_limite_chequeespecial()
