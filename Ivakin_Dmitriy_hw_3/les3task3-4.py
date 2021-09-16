def thesaurus_adv(*args):
    people_dict = {}
    for man in args:
        name_surname = man.split()
        name_first_letter = name_surname[0][0]
        surname_first_letter = name_surname[1][0]
        people_dict.setdefault(surname_first_letter, {})
        people_dict[surname_first_letter].setdefault(name_first_letter, []).append(man)
    return people_dict


print(
    thesaurus_adv("Иван Сергеев", "Прохор Анисимов", "Ивор Саркисян", "Жанна Серова", "Анна Савельева", "Петр Алексеев",
                  "Илья Иванов", "Дима Ивакин", "Денис Иващенко", 'Анна Селеста'))
