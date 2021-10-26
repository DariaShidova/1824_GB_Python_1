import itertools
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Соня', 'Олег', 'Станислав', 'Анатолий'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
p = ((tu, kl) for tu, kl in itertools.zip_longest(tutors, klasses) if tu)


print(type(p))
while 1 > 0:  # просто до StopIteration
    print(next(p))
