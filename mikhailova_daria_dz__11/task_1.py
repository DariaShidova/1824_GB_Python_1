from datetime import date


class Data:
    def __init__(self, data):
        self.data = data.split('-')

    @classmethod
    def type(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            return f"{type(day), day}\n{type(month), month}\n{type(year), year}"
        except ValueError:
            return f'неверная  : {data}'

    @staticmethod
    def valid(data):
        try:
            day, month, year = data.split('-')
            date(int(year), int(month), int(day))
            return 'это явно дата'
        except ValueError:
            return f'неверная дата :{data}'


print(Data.valid('11-17-2028'))
print(Data.valid('41-11-2026'))
print(Data.valid('01-11-2026'))
print(Data.type('17-02'))
