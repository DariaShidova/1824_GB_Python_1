class Cell:
    def __init__(self, numbs):
        self.numbs = int(numbs)

    def __add__(self, other):
        return self.numbs + other.numbs

    def __sub__(self, other):
        sub = self.numbs - other.numbs
        return sub if sub > 0 else '-'

    def __truediv__(self, other):
        return self.numbs // other.numbs

    def __mul__(self, other):
        return self.numbs * other.numbs

    def make_order(self, row):
        asterisk = ''
        for i in range(int(self.numbs / row)):
            asterisk += '*' * row + "\n"
        asterisk += '*' * (self.numbs % row)
        return asterisk


cell = Cell(134)
c = Cell(90)
d = Cell(30)
print(c + d)
print(c - d)
print(c / d)
print(c * d)
print(cell.make_order(15))
