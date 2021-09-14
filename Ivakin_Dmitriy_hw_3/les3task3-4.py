def thesaurus_adv(*args):
    people_dict = {}
    for man in args:
        word = man.split()
        surname = word[1][0]
        name = word[0][0]
        people_dict.setdefault(surname, {})
        if surname in people_dict:
            people_dict[surname].setdefault(name, []).append(man)
    return people_dict


print(thesaurus_adv("Иван Сергеев", "Ивор Саркисян", "Жанна Серова", "Анна Савельева", "Петр Алексеев", "Илья Иванов",
                    "Дима Ивакин", "Денис Иващенко", "Прохор Анисимов", 'Анна Селеста'))
