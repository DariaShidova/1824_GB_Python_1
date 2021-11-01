def type_logger(func):
    def type_write(*arg):
        result = []
        for i in arg:
            result.append(f'{func.__name__}({i}: {type(i)})')
        print(', '.join(result))
        return result

    return type_write


@type_logger
def calc_cube(x):
    return x ** 3  # не поняла что происходит с самой функцией где ее результат (сам куб числа)


a = (calc_cube(5, 9, "str"))


