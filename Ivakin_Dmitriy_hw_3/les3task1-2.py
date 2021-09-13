def num_translate(num):
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
        'Ten': 'Десять',

    }
    if num.capitalize() in translation:
        if num.islower():
            print(f'Перевод {num} на русский язык: {translation.get(num.capitalize()).lower()}.')
        else:
            print(f'Перевод {num} на русский язык: {translation.get(num)}.')
    else:
        print(f'Перевод {num} на русский язык: {translation.get(num)}.')


# num_translate(input('Введите на английском число от 0 до 10 для перевода на русский: '))
num_translate('Two')
num_translate('two')
num_translate('Ноль')
