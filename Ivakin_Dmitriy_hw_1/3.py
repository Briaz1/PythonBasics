# Версия с input:
num = input('Введите число для склонения слова "процент": ')
if len(num) > 1 and int(num[-2]) == 1 and 1 <= int(num[-1]) <= 9:
    print(f'{num} процентов')
elif int(num[-1]) == 1:
    print(f'{num} процент')
elif 2 <= int(num[-1]) <= 4:
    print(f'{num} процента')
elif 5 <= int(num[-1]) <= 9 or int(num[-1]) == 0:
    print(f'{num} процентов')

# Версия с range:
# for num in range(1, 101):
#     num = str(num)
#     if len(num) > 1 and int(num[-2]) == 1 and 1 <= int(num[-1]) <= 9:
#         print(f'{num} процентов')
#     elif int(num[-1]) == 1:
#         print(f'{num} процент')
#     elif 2 <= int(num[-1]) <= 4:
#         print(f'{num} процента')
#     elif 5 <= int(num[-1]) <= 9 or int(num[-1]) == 0:
#         print(f'{num} процентов')
