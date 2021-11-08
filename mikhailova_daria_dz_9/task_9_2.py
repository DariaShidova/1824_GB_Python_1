class Road:

    def __init__(self, length, width):
        self.weight = 25
        self.height = 5
        self._length = length
        self._width = width

    def mass(self):
        asphalt = (self._length * self._width * self.weight * self.height) / 1000
        return asphalt


r = Road(5000, 20)
print(r.mass())
