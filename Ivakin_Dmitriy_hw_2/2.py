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

# Обособление кавычками
for num in num_index:
    task_list.insert(num, '"')
    task_list.insert(num + 2, '"')
    for idx, _ in enumerate(num_index):
        num_index[idx] += 2

print(task_list)

# Обособляем числа кавычками

# cur_position = 1
# while cur_position < len(word_list):
#     word_list.insert(cur_position, "*")
#     # print(cur_position)
#     cur_position += 2
#     # print(word_list)
# print(word_list)
