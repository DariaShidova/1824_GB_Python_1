class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'{super().draw()}: {self.title}'


class Pencil(Stationery):
    def draw(self):
        return f'{super().draw()}: {self.title}'


class Handle(Stationery):
    def draw(self):
        return f'{super().draw()}: {self.title}'


pen = Pen('pen')
pencil = Pencil('pencil')
handle = Handle('handle')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
