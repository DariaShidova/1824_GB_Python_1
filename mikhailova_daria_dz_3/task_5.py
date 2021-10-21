import random


def get_jokes(n: int, replay=True) -> list or None:
    """
    Генерирует предложение из солов из 3х случайных слов,
    из разных списков.Возвращает список с предложениями в количестве указанных.
    При значении False - слова не повторяются, максимальное кол-во
    предложений равно длинне списка.
    """
    p = 0
    joke = []
    if replay is False:
        while 0 != len(adjective):  # пока длинна списка не будет равна нулю
            # перебераем списки и вытаскиваем рандомные слова
            for name, login, role in zip(random.choices(animal), random.choices(adjective), random.choices(job)):
                joke.append(f'{name} - {login} {role}')  # формируем предложение
                animal.remove(name)  # удаляем использованные  слова из списка
                adjective.remove(login)
                job.remove(role)
        return joke  # возвращаем список с предложениями
    else:
        while p <= n:
            for name, login, role in zip(random.choices(animal), random.choices(adjective), random.choices(job)):
                p += 1
                joke.append(f'{name} - {login} {role}')
        return joke


job = ['школьник', 'курьер', 'прораб', 'регионовед', 'рыбак']
animal = ['Анаконда', 'Заяц', 'Ленточник', 'Степпезавр', 'Чайка']
adjective = ['коммунистический', 'богатый', 'виновный', 'натуральный', 'былой']
print(get_jokes(7))
print(get_jokes(100, False))
