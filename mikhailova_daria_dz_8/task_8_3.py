def type_logger(func):
    def type_write(*arg):
        result = []
        for i in arg:
            result.append(f'{func.__name__}({i}: {type(i)})')
        print(', '.join(result))
        return arg

    return type_write


@type_logger
def calc_cube(x):
    return x ** 3  # не допоняла  с самой функцией ее результат (сам куб числа), нужно ли было его здесь возвращать


a = (calc_cube(5, 9, "str"))
