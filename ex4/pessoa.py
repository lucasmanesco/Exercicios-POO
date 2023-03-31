class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, envelheceu: int):
        self.idade += envelheceu
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, engordou: float):
        self.peso += engordou

    def emagrecer(self, emagreceu: float):
        self.peso -= emagreceu

    def crescer(self, crescimento: float):
        self.altura += crescimento

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r}, '\
            f'{self.peso!r}, {self.altura!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    p1 = Pessoa('Lucas', 28, 68.5, 1.75)
    p1.engordar(3)
    print(p1)
    p1.envelhecer(2)
    print(p1)
    p1.crescer(0.1)
    print(p1)
    p1.emagrecer(1)
    print(p1)
