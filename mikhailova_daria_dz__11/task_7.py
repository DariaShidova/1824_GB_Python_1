from __future__ import annotations


class ComplexNumber:

    def __init__(self, numbs: complex):
        self.numbs = numbs

    def __add__(self, other: ComplexNumber):
        return self.numbs + other.numbs

    def __mul__(self, other: ComplexNumber):
        return self.numbs * other.numbs


b = ComplexNumber(11 + 7j)
a = ComplexNumber(12 + 9j)
print(b + a)
print(b * a)