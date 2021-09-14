def thesaurus(*args):
    dct = {}
    for el in args:
        dct.setdefault(el[0], []).append(el)

    print(dct)
    print(args)


thesaurus('Дима', 'Саша', 'Маша', 'Даша', 'Даша', 'Мага', 'Мойша', 'Ася')
