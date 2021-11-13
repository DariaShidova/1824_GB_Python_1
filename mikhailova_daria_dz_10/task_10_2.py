from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, parameter):
        self.parameter = parameter

    @property
    def general(self):
        return f'Сумма : {self.parameter / 6.5 + 0.5 + 2 * self.parameter + 0.3 :.2f}'


class Coat(Clothes):
    def consumption(self):
        return f'Для пальто: {self.parameter / 6.5 + 0.5 :.2f} ткани'


class Costume(Clothes):
    def consumption(self):
        return f'Для костюма: {2 * self.parameter + 0.3 :.2f} ткани'


a = Coat(10)
b = Costume(2)
print(a.consumption())
print(b.consumption())



