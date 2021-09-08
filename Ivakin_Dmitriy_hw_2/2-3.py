task_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
num_index = []  # список для запоминания индексов подходящих под условие элементов (для обособления кавычками)
# Дополняем числа до двух целочисленных разрядов
for idx, word in enumerate(task_list):
    found_num = []
    for symbol in word:
        if ord(symbol) in range(49, 58) or symbol == '+' or symbol == '-':
            if symbol.isdigit():
                found_num.append(symbol)
        else:
            found_num = []
            break
    if len(found_num) > 0:
        task_list[idx] = word.replace(''.join(found_num), f"{''.join(found_num):0>2}")
        num_index.append(idx)
print(task_list)

# Сохраняем актуальные индексы чисел для вывода строки и расставления кавычек
i = 1
for idx, _ in enumerate(num_index):
    num_index[idx] += i
    i += 2
print(num_index)

# Обособление кавычками
for idx, num in enumerate(num_index):
    task_list.insert(num - 1, '"')
    task_list.insert(num + 1, '"')
print(task_list)

# Выводим строку
task_str = ''
for idx, word in enumerate(task_list):
    if idx == 0:
        task_str = f'{task_str}{word.capitalize()}'
    elif idx in num_index:
        task_str = f'{task_str} "{word}"'
    elif word == '"':
        continue
    else:
        task_str = f'{task_str} {word}'
print(task_str)






