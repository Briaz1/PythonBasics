given_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
numbers_index = []  # список для запоминания индексов подходящих под условие элементов (для обособления кавычками)
# Дополняем числа до двух целочисленных разрядов
for idx, word in enumerate(given_list):
    found_num = []
    for symbol in word:
        if ord(symbol) in range(49, 58) or symbol == '+' or symbol == '-':
            if symbol.isdigit():
                found_num.append(symbol)
        else:
            found_num = []
            break
    if len(found_num) > 0:
        given_list[idx] = word.replace(''.join(found_num), f"{''.join(found_num):0>2}")
        numbers_index.append(idx)

# Сохраняем актуальные индексы чисел для вывода строки и расставления кавычек
i = 1
for idx, _ in enumerate(numbers_index):
    numbers_index[idx] += i
    i += 2

# Обособление кавычками
for idx, num in enumerate(numbers_index):
    given_list.insert(num - 1, '"')
    given_list.insert(num + 1, '"')
print(given_list)

# Выводим строку
given_string = ''
for idx, word in enumerate(given_list):
    if idx == 0:
        given_string = f'{given_string}{word.capitalize()}'
    elif idx in numbers_index:
        given_string = f'{given_string} "{word}"'
    elif word == '"':
        continue
    else:
        given_string = f'{given_string} {word}'
print(given_string)
