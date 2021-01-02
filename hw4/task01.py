from sys import argv

def calc_salary(work_time: int, money_per_hour: float, bonus: float) -> float:
    """ Возвращает зарплату сотрудника.
    На входе: отработанное время (в часах), часовая ставка (рублей в час) и премия.
    На выходе: итоговая зарплата.
    """
    return work_time * money_per_hour + bonus

name_script, worked_hours, salary_per_hour, bonus = argv

print('\nЗаработная плата сотрудника: ' \
     f'{calc_salary(int(worked_hours), float(salary_per_hour), float(bonus))}')