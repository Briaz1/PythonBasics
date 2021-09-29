import json
from itertools import zip_longest


def users_hobby_dict(users_file, hobby_file):
    with open(users_file, 'rt', encoding='utf-8') as users, \
            open(hobby_file, 'rt', encoding='utf-8') as hobby, \
            open('users_hobby.csv', 'wt', encoding='utf-8') as uh:
        # Кортеж, потому что ключи должно быть неизменяемым
        name_gen = (tuple(user.replace('\n', '').split(',')) for user in users)
        interest_gen = (interest.replace('\n', '').split(',') for interest in hobby)
        for name, interest in zip_longest(name_gen, interest_gen):
            if name is None:
                exit(1)
            uh.write(f'{name}: {interest}\n')

users_hobby_dict('users.csv', 'hobby.csv')

# with open('users_hobby.json', 'rt', encoding='utf-8') as hn:
#     a = json.load(hn)
