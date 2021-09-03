declination_1 = [1, 21]
declination_2 = [2, 3, 4, 22, 23, 24]
declination_3 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30]

for num in range(1, 31):
    if num in declination_1:
        print(f'{num} процент.')
    elif num in declination_2:
        print(f'{num} процента.')
    else:
        print(f'{num} процентов.')


