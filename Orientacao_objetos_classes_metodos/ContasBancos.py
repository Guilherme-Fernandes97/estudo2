from datetime import datetime
import pytz


class ContaCorrente:

    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

    Atributos:
        nome (str): Nome do Cliente
        cpf (str): CPF do Cliente
        agencia: Agencia responsável pela conta do cliente
        num_conta: Número da conta corrente do cliente
        saldo: Saldo disponível na conta do cliente
        limite: Limite de cheque especial daquele cliente
        transacoes: Histórico de transações do cliente

    """

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self._limite = None
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []

    def consultar_saldo(self):
        print(f'Seu saldo atual é de R${self._saldo:,.2f}')

    def depositar(self, valor):
        self._saldo = + valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor.')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequeespecial(self):
        print(f'Seu limite de Cheque Especial é de R${self._limite_conta():,.2f}')

    def consultar_historico_transacoes(self):
        print('Histórico de Transações:')
        print('Valor, Saldo, Data e Hora')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        if self._saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para transferir esse valor.')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
            conta_destino._saldo += valor
            conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


# Programa

conta_Lira = ContaCorrente("Lira", "111.222.333-45", 1234, 34062)
conta_Lira.consultar_saldo()

# Depositando dinheiro na conta
conta_Lira.depositar(10000)
conta_Lira.consultar_saldo()

conta_Lira.consultar_saldo()
conta_Lira.consultar_limite_chequeespecial()

print('-' * 20)

conta_Lira.consultar_historico_transacoes()

print('-' * 20)

conta_maeLira = ContaCorrente("Beth", "111.333.444-56", 1234, 40062)
conta_Lira.transferir(1000, conta_maeLira)

conta_Lira.consultar_historico_transacoes()
conta_maeLira.consultar_historico_transacoes()
