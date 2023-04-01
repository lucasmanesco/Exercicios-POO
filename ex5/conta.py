class Conta:
    def __init__(self, conta: int, nome: str, saldo: float = 0):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, valor):
        self.saldo += valor
        print(f'Depósito realizado: R${valor:.2f} - Saldo: R${self.saldo:.2f}')

    def saque(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente para essa operação.')
        self.saldo -= valor
        print(f'Saque realizado: R${valor:.2f} - Saldo: R${self.saldo:.2f}')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.conta!r}, {self.nome!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    c1 = Conta(8160, 'Lucas', 150)

    c1.alterar_nome('Lucas Manesco')
    c1.saque(50)
    c1.saque(100)
    c1.deposito(20)
    print(c1)
