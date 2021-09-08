task_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов', "+привет1друг2",
             '-45']
num_index = []
# Дополняем числа до двух целочисленных разрядов
for idx, word in enumerate(task_list):
    found_num = []
    for symbol in word:
        if symbol.isdigit() is True:
            found_num.append(symbol)
    if len(found_num) > 0:
        task_list[idx] = word.replace(''.join(found_num), f"{''.join(found_num):0>2}")
        num_index.append(idx)
for num in num_index:
    task_list.insert(num, '"')
    task_list.insert(num + 2, '"')
    for idx, _ in enumerate(num_index):
        num_index[idx] += 2

print(task_list)
print(num_index)

# Обособляем числа кавычками

# cur_position = 1
# while cur_position < len(word_list):
#     word_list.insert(cur_position, "*")
#     # print(cur_position)
#     cur_position += 2
#     # print(word_list)
# print(word_list)
