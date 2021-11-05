class Car:

    def __init__(self, name, speed, color, is_police: bool):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} едет.'

    def stop(self):
        return f'{self.name} остановилась.'

    def turn(self, direction):
        return f'{self.name} поворачивает {direction}'

    def show_speed(self):
        return f'скорость: {self.speed}'

    def police(self):
        if self.is_police:
            return 'остановила полиция: Документики?'
        else:
            return ''


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'{super().show_speed()} - превышении скорости!'
        else:
            return super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'{super().show_speed()} - превышении скорости!'
        else:
            return super().show_speed()


class PoliceCar(Car):
    def show_speed(self):
        return f'{super().show_speed()}, могу ехать как захочу'

    def police(self):
        return 'остановила полиция: я ваш коллега'


t = TownCar('маленькая машина', 62, 'Белая', True)
s = SportCar('спортивная машина', 237, 'Красная', False)
w = WorkCar('грузовик', 70, 'Зеленый', False)
p = PoliceCar('бобик', 800, 'Серо-синий', True)

print(f'{t.color} {t.go()} \n{t.show_speed()} \n{t.turn("на лево")}\n{t.police()}\n{t.stop()}\n')
print(f'{s.go()}\n{s.show_speed()}\n{s.stop()}\n')
print(f'{p.go()}\n{p.turn("на право")}\n{p.show_speed()}\n{p.police()}')

