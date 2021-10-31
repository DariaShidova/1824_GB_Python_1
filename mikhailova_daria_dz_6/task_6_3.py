import itertools
import sys
hobby_list = []
user_list = []


with open('text_users_hobby.txt', 'w', encoding='utf-8') as text, open('users.csv', encoding='utf-8') as user, open(
        "hobby.csv", encoding='utf-8')as hobby:
    for u in user:
        u = ''.join(u.split('\n'))
        user_list.append(' '.join(u.split(',')))

    for h in hobby:
        hobby_list.append(''.join(h.split('\n')))

    for tu, kl in itertools.zip_longest(user_list, hobby_list):
        if tu:
            version_dict = {tu: kl}
            text.write(f"{str(version_dict)} \n")
        if not tu:
            sys.exit(1)
