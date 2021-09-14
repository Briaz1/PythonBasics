def thesaurus(*args):
    dct = {}
    for el in args:
        word = el.split()
        sur = word[1][0]
        name = word[0][0]
        dct.setdefault(sur, {})
    for el in args:
        word = el.split()
        sur = word[1][0]
        name = word[0][0]
        if sur in dct:
            dct[sur].setdefault(name, []).append(el)

    print(dct)


thesaurus("Иван Сергеев", "Ивор Саркисян", "Жанна Серова", "Анна Савельева", "Петр Алексеев", "Илья Иванов", "Дима Ивакин", "Денис Иващенко")
