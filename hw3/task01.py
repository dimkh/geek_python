def division_numbers(first_num: float, second_num: float) -> float:
    """ Возвращает частное от деления.
    Первое число - делимое, второе - делитель.
    На входе должны быть числа (проверки нет - выполнена ранее).
    """
    try:
        result = first_num / second_num
    except ZeroDivisionError:
        return 'Делить на ноль нельзя!'
    return result

a = input('\nВведите первое число: ')
b = input('Введите второе число: ')

if a.isdigit() and b.isdigit():
    print(f'\nРезультат деления {a} / {b}: {division_numbers(float(a), float(b))}')
else:
    print(f'\nОшибка! Ввести нужно 2 числа!')
