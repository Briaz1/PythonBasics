# Функция для вывода результатов разных решение
def printing(gen):
    print(type(gen))  # Показывает что функция возвращает генератор
    for el in gen:
        print(el)
    print('-' * 35)


# Решение через zip:
def tutors_classes_zip(tutors_list, classes_list):
    while len(tutors_list) > len(classes_list):
        classes_list.append(None)
    for name, cl in zip(tutors_list, classes_list):
        yield name, cl


# Решение через enumerate:
def tutors_classes_enum(tutors_list, classes_list):
    for idx, name in enumerate(tutors_list):
        if idx < len(classes_list):
            yield name, classes_list[idx]
        else:
            yield name, None


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Фёдор', 'Матвей', 'Анна'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

printing(tutors_classes_zip(tutors, classes))
printing(tutors_classes_enum(tutors, classes))
# Решение генераторным выражением
printing(((name, classes[idx] if idx < len(classes) else None) for idx, name in enumerate(tutors)))
