def odd_nums(n:int):
    for num in range(n + 1):
        if num % 2 != 0:
            yield num


p = odd_nums(int(input()))
print(type(p))

while 1 > 0:   # просто до StopIteration
    print(next(p))




