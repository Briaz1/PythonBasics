def num_translate_adv(num):
    translation = {
        'Zero': 'Ноль',
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре',
        'Five': 'Пять',
        'Six': 'Шесть',
        'Seven': 'Семь',
        'Eight': 'Восемь',
        'Nine': 'Девять',
        'Ten': 'Десять'
    }

    if num.capitalize() in translation and num.islower():
        print(f'Перевод "{num}" на русский язык: {translation.get(num.capitalize()).lower()}.')
    else:
        print(f'Перевод "{num}" на русский язык: {translation.get(num)}.')


num_translate_adv(input('Введите на английском число от 0 до 10 для перевода на русский: '))
