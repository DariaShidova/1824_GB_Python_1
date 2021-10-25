import sys
def proceeds(hov):
    with open('bakery.csv', 'a', encoding='utf-8')as bakery:
        bakery.write(f'{str(hov)}\n')
if __name__ == '__main__' :
    proceeds(sys.argv[1])