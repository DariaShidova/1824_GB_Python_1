def thesaurus(name):
    """Возвращает словарь, где заглавная буква это ключ"""
    rus_letter = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧЩЪЫЬЭЮЯ'
    name_dict = {}
    for n in name:
        for i in rus_letter:
            if i in n:
                if i not in name_dict:
                    name_dict.setdefault(i, [n])
                elif i in name_dict:
                    key_i = list(name_dict.pop(i))
                    key_i.append(n)
                    name_dict.setdefault(i, key_i)
    return name_dict


name_case = ('Марина', 'Оскар', 'Терентий', 'Мифодий', 'Ольга', 'Валентин', 'Виктория', 'Дарья', 'Ратмир', 'Афанасий',
             "Аля", 'Петя', 'Аркадий')
print(thesaurus(name_case))
