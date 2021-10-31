result = []
address = []


with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for row in f:
        d = ''.join(row.split('"')).split(" ")
        result.append((d[0], d[5], d[6]))
        address.append(d[0])


#print(result)

how_many = {i: address.count(i) for i in address}
value = 1
key = ''
for _ in how_many:
    if how_many[_] > value:
        value = how_many[_]
        key = _


print(f'ip Спамера - {key}, заходил - {value} раз')
