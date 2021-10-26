n = int(input())
odd_nums = (num for num in range(n + 1) if num % 2 != 0)
print(type(odd_nums))

while 1 > 0:  # просто до StopIteration
    print(next(odd_nums))
