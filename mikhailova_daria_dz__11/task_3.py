class Error(Exception):
    def __init__(self):
        pass


class Check:
    def __init__(self):
        self.numbs = []

    def check_value(self):
        while True:
            try:
                try:
                    number = int(input('Введите число: '))
                    answer = input(f'Добавили "{number}" в список.Добавим еще? y/n: ').lower()
                    self.numbs.append(number)
                    if answer == 'n':
                        print(self.numbs)
                        break
                except ValueError:
                    raise Error
            except Error:
                answer = input(f'Это не число,продолжим? y/n: ').lower()
                if answer == 'n':
                    print(self.numbs)
                    break
                else:
                    self.check_value()


a = Check()
a.check_value()