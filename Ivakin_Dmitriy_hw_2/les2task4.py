list_of_employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                     'директор аэлита']
for el in list_of_employees:
    print(f'Привет, {el.split()[-1].capitalize()}!')
