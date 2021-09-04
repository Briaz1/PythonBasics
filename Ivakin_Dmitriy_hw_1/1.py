#Задание 1
duration = int(input('Enter time in seconds: '))

days = duration // 86400
hours = duration % 86400 // 3600
minutes = duration % 3600 // 60
seconds = duration % 60

time_unit = [f'{days}d', f'{hours}h', f'{minutes}m', f'{seconds}s']
time = f'{duration} seconds = '

for idx, el in enumerate(time_unit):
    if int(el[0]) != 0:
        time += time_unit.copy().pop(idx) + " "

print(time)
