class Tv:
    def __init__(self, canal: int, volume: int = 0, canais: list = []):
        self.canal = canal
        self.volume = volume
        self.canais = canais

    def mudar_canal(self, novo_canal):
        if novo_canal in self.canais:
            self.canal = novo_canal
            return f'Canal atual: {self.canal}'
        return 'Canal não encontrado.'

    def aumentar_volume(self, vol):
        self.volume += vol
        if self.volume > 80:
            return 'Volume muito alto. Cuidado com os ouvidos!'

    def diminuir_volume(self, vol):
        self.volume -= vol
        if self.volume < 20:
            return 'Volume muito baixo. Faça silêncio para ouvir!'

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.canal!r}, {self.volume!r}, {self.canais!r})'
        return f'{class_name} {attrs}'


if __name__ == '__main__':
    tv1 = Tv(16, 35, [16, 20, 38, 39, 48, 51, 61, 62])
    print(tv1.mudar_canal(51))
    print(tv1.aumentar_volume(50))
    print(tv1.diminuir_volume(80))
    print(tv1)
