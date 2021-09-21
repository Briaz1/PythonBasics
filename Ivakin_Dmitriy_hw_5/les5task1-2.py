# Я не уверен, что правильно понял что нужно сделать, но если я понял правильно - цель была понять, что через yield
# мы возвращаем элемент генератора, созданного вручную, а через return мы возвращаем генераторное выражение.

def odd_numbers_gen_yield(num):
    for odd_num in range(1, num + 1, 2):
        yield odd_num


def odd_numbers_gen_2_return(num):
    return (odd_num for odd_num in range(1, num + 1, 2))


yield_list = []
return_list = []
for el in odd_numbers_gen_yield(15):
    yield_list.append(el)

for el in odd_numbers_gen_2_return(20):
    return_list.append(el)

print(yield_list)
print(return_list)
