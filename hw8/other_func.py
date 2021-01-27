import my_except as me

# Список отделов компании
departments = ['storage', 'accounting', 'soft development', 'support']


def is_digit(dig_str: str) -> int:
    """ Проверка строки на натуральное число больше нуля
    На входе: число в виде строки
    На выходе: преобразованное число.
    При ошибке генерируем исключение.
    """
    if not dig_str.isdigit():
        raise me.StorageError("\nОшибка при вводе количества!")
    result = int(dig_str)
    if result == 0:
        raise me.StorageError("\nКоличество должно быть больше нуля!")
    return result


def choice_department() -> str:
    """ Выбор подразделения компании из списка.
    На выходе: наименование подразделения или пустая строка, если не выбрал.
    """
    num = 1
    result = ''
    print('\n0 - Выход без выбора')
    for i in range(num, len(departments)):
        print(f'{num} - {departments[i]}')
        num += 1
    while True:
        choice = input('Выберите отдел: ')
        if choice.isdigit() and 0 < int(choice) < num:
            result = departments[int(choice)]
            break
    return result
