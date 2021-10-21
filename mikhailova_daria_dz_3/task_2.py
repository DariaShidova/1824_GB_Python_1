import string
translator_num = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                  'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate_adv(user_n: str) -> str:
    """Возвращает перевод числового значения от нуля до 10 по ключу,если ключа нет возврощает None"""
    if user_n not in translator_num:
        for n in string.ascii_uppercase:
            if n in str(user_n):
                if user_n.lower() not in translator_num:
                    return translator_num.get(user_n)
                else:
                    return (translator_num[user_n.lower()]).capitalize()
    else:
        return translator_num[user_n]


translate = num_translate_adv(str(input('введите число для перевода')))
print(translate)
