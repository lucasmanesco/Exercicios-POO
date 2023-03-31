class Quadrado:
    def __init__(self, lado: float):
        self.lado = lado

    def mudar_lado(self, novo_lado):
        self.lado = novo_lado
        return self.lado

    def mostrar_lado(self):
        print(f'O lado tem {self.lado}cm.')

    def calcular_area(self):
        area = self.lado ** 2
        return f'A área tem {area}cm².'

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.lado!r})'
        return f'{class_name}, {attrs}'


if __name__ == '__main__':
    q1 = Quadrado(10)
    print(q1)
    print(q1.lado)
    q1.mudar_lado(20)
    q1.mostrar_lado()
    print(q1.calcular_area())
