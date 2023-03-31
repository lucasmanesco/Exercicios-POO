class Retangulo:
    def __init__(self, comp: float, larg: float):
        self.comp = comp
        self.larg = larg

    def mudar_comp(self, novo_comp):
        self.comp = novo_comp
        return self.comp

    def mudar_larg(self, nova_larg):
        self.larg = nova_larg
        return self.larg

    def exibe_medidas(self):
        print(f'O retângulo tem as medidas: {self.comp} x {self.larg}cm.')

    def calc_area(self):
        area = self.comp * self.larg
        return area

    def calc_perimetro(self):
        perimetro = 2*(self.comp + self.larg)
        return perimetro

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.comp!r}, {self.larg!r})'
        return f'{class_name}, {attrs}'


if __name__ == '__main__':
    comp = float(input('Informe o comprimento do local em metros: '))
    larg = float(input('Informe a largura do local em metros: '))
    p = float(input('Qual piso será utilizado? (m): '))

    area_piso = p ** 2

    r = Retangulo(comp, larg)

    area_local = r.calc_area()
    qtd_piso = area_local / area_piso

    perim_local = r.calc_perimetro()
    qtd_rodape = perim_local

    print(f'Você vai precisar de {qtd_piso} pisos.')
    print(f'Você vai precisar de {qtd_rodape}m de rodapé.')
