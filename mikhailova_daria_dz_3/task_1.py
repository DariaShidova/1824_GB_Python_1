translator_num = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                  'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(user_num: str) -> str:
    """Возвращает перевод числового значения от нуля до 10 по ключу,если ключа нет возврощает None"""
    if user_num in translator_num:
        return translator_num[user_num]
    else:
        return translator_num.get(user_num)


translate = num_translate(input('введите число для перевода'))
print(translate)
