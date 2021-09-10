price_list = [28.5, 74.08, 1.25, 56.99, 100.8]
price_str = ''

# Выводим список в строку по условию задания
for idx, el in enumerate(price_list):
    price = str(el).split('.')
    if idx is len(price_list) - 1:
        price_str = f'{price_str}{price[0]:0>2} руб {price[-1]:0>2} коп.'
    else:
        price_str = f'{price_str}{price[0]:0>2} руб {price[-1]:0>2} коп, '
print(price_str)
print(id(price_list))
price_list.sort()
print(id(price_list))
