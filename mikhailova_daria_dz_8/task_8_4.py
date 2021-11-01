def val_checker(arg_decor):
    def _val_checker(func):
        def wrapper(*args):
            i = args[0]
            result = func(i)
            if arg_decor(i):
                return result
            else:
                raise ValueError(f'wrong val:{i}')

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x: int):
    return x ** 3


print(calc_cube(11))
print(calc_cube(-11))
