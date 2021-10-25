import sys


def deduction(a):
    with open('bakery.csv', encoding='utf-8') as f:
        text = f.readlines()
        arg = a[1:]
        how_arg = len(arg)
        if how_arg > 0:
            for _ in arg:
                flag = _.isdigit()
            if flag:
                start = int(arg[0]) - 1
                if how_arg == 1:
                    print(''.join(text[start:]))
                elif how_arg >= 2:
                    stop = int(arg[1])
                    print(''.join(text[start:stop]))
            else:
                sys.exit()
        else:
            print(''.join(text))


if __name__ == '__main__':
    deduction(sys.argv)
