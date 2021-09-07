task_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for idx, word in enumerate(task_list):
    found_num = []
    for symbol in word:
        if symbol.isdigit() is True:
            found_num.append(symbol)
    if len(found_num) > 0:
        task_list[idx] = task_list[idx].replace(''.join(found_num), f"{''.join(found_num):0>2}")
print(task_list)

# task_list[idx] = f'{word:0>2}'
#             if len(word) > 1:
#                 break
# print(task_list)

# word_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# for word in word_list:
#     found_num = []
#     for symb in word:
#         if symb.isdigit() is True:
#             found_num.append(symb)
#     if len(found_num) > 0:
#         print("Found number {:0>2}".format(''.join(found_num)))

# 49
# 50
# 51
# 52
# 53
# 54
# 55
# 56
# 57
