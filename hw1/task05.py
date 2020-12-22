income = float(input('\nВведите выручку фирмы: '))
expenses = float(input('Введите затраты фирмы: '))

fin_result = income - expenses
if fin_result > 0:
    print(f'\nПоздравляю! Ваша фирма получила прибыль в размере: {fin_result}')
    print(f'Рентабельность составила: {(fin_result / income):.2f}')
    staff = int(input('\nВведите количество работников фирмы: '))
    print(f'Прибыль в расчёте на одного сотрудника составила: {(fin_result / staff):.2f}\n')
elif fin_result == 0:
    print(f'\nВаша фирма сработала в ноль. Как дальше развиваться?\n')
else:
    # Минус в финансовом результате при убытках не убираю
    # Если нужно без минуса - просто умножить на (-1)
    print(f'\nУпс! Ваша фирма фиксирует убыток в размере: {fin_result}\n')