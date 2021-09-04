numbers = range(1, 1001)
cube_numbers = []
for num in numbers:
    cube_numbers.append(num ** 3)

# Часть a:
numbers_sum_a = 0
for idx, number in enumerate(cube_numbers):
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    if digit_sum % 7 == 0:
        numbers_sum_a += cube_numbers[idx]
print(f'a ver1. Sum of multiples of seven numbers - {numbers_sum_a}.')

# Часть b и с:
numbers_sum_b = 0
for idx, number in enumerate(cube_numbers):
    digit_sum = 0
    number_17 = number + 17
    while number_17 > 0:
        digit_sum += number_17 % 10
        number_17 //= 10
    if digit_sum % 7 == 0:
        numbers_sum_b += cube_numbers[idx] + 17
print(f'b and c ver1. Sum of multiples of seven numbers - {numbers_sum_b}.')

# Часть a через str:
numbers_sum_a_str = 0
for el in cube_numbers:
    el = str(el)
    digit_sum = 0
    for digit in el:
        digit_sum += int(digit)
    if digit_sum % 7 == 0:
        numbers_sum_a_str += int(el)
print(f'a ver2. Sum of multiples of seven numbers - {numbers_sum_a_str}.')

# Часть b и с через str:
numbers_sum_b_str = 0
for el in cube_numbers:
    el_17 = el + 17
    el_17 = str(el_17)
    digit_sum = 0
    for digit in el_17:
        digit_sum += int(digit)
    if digit_sum % 7 == 0:
        numbers_sum_b_str += int(el_17)
print(f'b and c ver2. Sum of multiples of seven numbers - {numbers_sum_b_str}.')
