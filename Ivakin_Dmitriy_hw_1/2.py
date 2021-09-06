cube_numbers = []
for num in range(1, 1001, 2):
    cube_numbers.append(num ** 3)

# Часть a.
numbers_sum_a = 0
for idx, number in enumerate(cube_numbers):
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    if digit_sum % 7 == 0:
        numbers_sum_a += cube_numbers[idx]
print(f'Sum of multiples of seven numbers - {numbers_sum_a}.')

# Часть b и с.
numbers_sum_b = 0
for idx, number in enumerate(cube_numbers):
    digit_sum = 0
    number_17 = number + 17
    while number_17 > 0:
        digit_sum += number_17 % 10
        number_17 //= 10
    if digit_sum % 7 == 0:
        numbers_sum_b += cube_numbers[idx] + 17
print(f'Sum of multiples of seven numbers - {numbers_sum_b}.')
