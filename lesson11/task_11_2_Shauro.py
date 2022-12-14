"""
2. Реализуйте класс который представляет собой универсальный интерфейс по представлению температуры в
шкалах Цельсия/Кельвина/Фаренгейта и поддерживает конвертацию значений температуры между этими шкалами
"""


class Swap:
    """
    Класс для конвертации температуры
    """
    def __init__(self):
        self.F = 32
        self.K = 273.15
        self.C = 0

    def Celsius(self, C):
        self.C = C
        self.K = C + 273.15
        self.F = C * (9 / 5) + 32

    def Kelvin(self, K):
        self.K = K
        self.C = K - 273.15
        self.F = (K - 273.15) * (9 / 5) + 32

    def Fahrenhei(self, F):
        self.F = F
        self.C = (F - 32) * (5 / 9)
        self.K = (F - 32) * (5 / 9) + 273.15


swap_1 = Swap()
swap_1.Celsius(57)
print(swap_1.K)
swap_1.Kelvin(330.15)
print(swap_1.C)
print(swap_1.F)
