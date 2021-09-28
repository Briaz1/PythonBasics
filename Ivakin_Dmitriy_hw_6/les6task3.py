import json


def users_hobby_dict(users_file, hobby_file):
    with open(users_file, 'rt', encoding='utf-8') as users, open(hobby_file, 'rt', encoding='utf-8') as hobby:
        name = [name.replace('\n', '') for name in users.readlines()]
        interest = [interest.replace('\n', '') for interest in hobby.readlines()]
    with open('users_hobby.json', 'wt', encoding='utf-8') as uh:
        if len(name) < len(interest):
            users_hobby = {name: interest for name, interest in zip(name, interest)}
            json.dump(users_hobby, uh)
            print(users_hobby)
            exit(1)
        else:
            users_hobby = dict.fromkeys(name)
            users_hobby.update(zip(name, interest))
            print(users_hobby)
            json.dump(users_hobby, uh)


users_hobby_dict('users.csv', 'hobby.csv')
