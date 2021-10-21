msg_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for n in msg_list:
    if '0' <= n <= '9':
        i = msg_list.index(n)
        msg_list[i] = n.zfill(2)
        msg_list.insert(i + 1, '"')
    elif '+0' <= n <= '+9':
        i = msg_list.index(n)
        msg_list[i] = n.zfill(3)
        msg_list.insert(i + 1, '"')
msg_list.reverse()

for n in msg_list:
    if '0' <= n <= '9':
        i = msg_list.index(n)
        msg_list.insert(i + 1, '"')
    elif '+0' <= n <= '+9':
        i = msg_list.index(n)
        msg_list.insert(i + 1, '"')

message = ' '.join(msg_list[::-1])
print(message)
