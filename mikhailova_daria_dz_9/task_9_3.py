class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'Дoход : {self._income["wage"] + self._income["bonus"]}'


p = Position('Артем', 'Какорин', 'продавец', '15000', '600')
print(p.get_full_name(), p.position, p.get_total_income())
