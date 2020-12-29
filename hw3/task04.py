def exp_per_stars(a: float, b:float) -> float:
    """ Возведение a в степень b, с использованием оператора **
    b - отрицательное (проверка не производится)
    На входе: основание и отрицательный показатель
    На выходе: итог возведения в степень
    """
    return 1 / (a ** abs(b))

def exp_per_cycle(a: float, b:int) -> float:
    """ Возведение a в степень b, с использованием цикла
    b - отрицательное целое (проверка не производится)
    На входе: основание и отрицательный целый показатель
    На выходе: итог возведения в степень
    """
    result = 1
    for i in range(abs(b)):
        result *= a
    return 1 / result

print(f'\nВычисление степени через "**": {exp_per_stars(2, -3)}')
print(f'Вычисление степени через цикл: {exp_per_cycle(2, -3)}')