def sum_2max(a: float, b:float, c:float) -> float:
    """ Возвращает сумму двух наибольших чисел из трех входящих.
    На входе: 3 числа (проверка не производится).
    На выходе: сумма двух наибольших.
    """
    all_numbers = [a, b, c]
    all_numbers.sort()
    return all_numbers[1] + all_numbers[2]

print(f'\nСумма двух наибольших чисел: {sum_2max(5, 3, 8)}')