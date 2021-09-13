number_list = [28.5, 74.08, 1.25, 56.99, 100.8, 14.0, 45.78, 69.2, 136.74, 29.91]


# Создаём функцию для вывода (понимаю что не проходили, но по факту просто дублирование кода убираю)
def price_list_output(price_list, sort):
    price_str = ''
    for idx, el in enumerate(price_list):
        price = str(el).split('.')
        if idx is len(price_list) - 1:
            price_str = f'{price_str}{price[0]:0>2} руб {price[-1]:0>2} коп.'
        else:
            price_str = f'{price_str}{price[0]:0>2} руб {price[-1]:0>2} коп, '
    print(f'{sort}{price_str}')


# Выводим оригинальный список и его id
price_list_output(number_list, 'Оригинальный список: ')
print(f'ID оригинального списка: {id(number_list)}.')

# Сортируем по возрастанию, выводим отсортированный список и его id
number_list.sort()
price_list_output(number_list, 'Список по возрастанию: ')
print(f'ID списка по возрастанию: {id(number_list)}.')

# Сортируем по убиванию и видим, что функция sorted меняет id
price_list_output(sorted(number_list, reverse=True), 'Список по убиванию: ')
print(f'ID списка по убыванию: {id(sorted(number_list, reverse=True))}.')

# Выводим список 5 самых дорогих товаров в уже остортированном списке.
price_list_output(number_list[5:], '5 самых больших цен в списке: ')
