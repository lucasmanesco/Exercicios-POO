class Bola:
    def __init__(self, cor: str, circ: float, material: str):
        self.cor = cor
        self. circ = circ
        self.material = material

    def troca_cor(self, nova_cor: str):
        self.cor = nova_cor
        return self.cor

    def mostra_cor(self):
        print(f'A cor é {self.cor}')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.cor!r}, {self.circ!r}, {self.material!r})'
        return f'{class_name}, {attrs}'


if __name__ == '__main__':

    b1 = Bola('preta', 50, 'couro')

    print(b1)
    print(b1.cor)
    print(b1.circ)
    print(b1.material)

    b1.troca_cor('vermelha')
    b1.mostra_cor()
