price_list = [36.9, 21.71, 65.3, 46.9, 99.09, 87.1, 14.09, 17, 53.01, 44.04]
price_list_2 = []
for n in price_list:
    i = price_list.index(n)
    a = int(((price_list[i]) * 100) % 100)
    price_list_2.append(a)
price_list_2[:] = [n.__str__() for n in price_list_2]

for n in price_list_2:
    i = price_list_2.index(n)
    price_list_2[i] = n.zfill(2)

price_list[:] = [n.__int__()for n in price_list]
price_list[:] = [n.__str__()for n in price_list]

result_list = []
r = 0
while r < len(price_list):
    # noinspection PyTypeChecker
    result_list.append(price_list[r] + ' руб ' + price_list_2[r] + ' коп')
    r += 1

message = ','.join(result_list)
print('Оригинальный порядок:', message)
result_list = message.split(',')
print(id(result_list[1]), (id(result_list)))
result_list.sort()
print('По возрастанию:', ', '.join(result_list))
print(id(result_list[3]), (id(result_list)))
result_list = sorted(result_list, reverse=True)
print('По убыванию:', ', '.join(result_list))
print('5 самых дорогих:', ', '.join(result_list[:-5]))
