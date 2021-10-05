cube_list = []
number = 0
while number <= 1000:
    if not number % 2 == 0:
        number = number+1
    else:
        number = number + 1
        cub = number ** 3
        cube_list.append(cub)
print(cube_list)
i = 0
remainder_sum = 0
main_sum_7 = 0
for n in cube_list:
    i = n
    while n != 0:
        remainder = n % 10
        remainder_sum = remainder + remainder_sum
        n = n//10
    if remainder_sum % 7 == 0:
        main_sum_7 += i
    remainder_sum = 0
print(main_sum_7)
cube_list[:] = [n+17 for n in cube_list]
print(cube_list)

i = 0
remainder_sum = 0
main_sum_7 = 0
for n in cube_list:
    i = n
    while n != 0:
        remainder = n % 10
        remainder_sum = remainder + remainder_sum
        n = n//10
    if remainder_sum % 7 == 0:
        main_sum_7 += i
    remainder_sum = 0
print(main_sum_7)
