def gen_fact(n: int):
    """ Генератор для вычисления факториала числа
    На входе: число
    На выходе: генератор для вычисления факториала
    """
    i = 1
    while i <= n:
        yield i
        i += 1

def fact(n: int) -> int:
    """ Вычисление факториала числа с помощью генератора
    На входе: число
    На выходе: факториал числа
    """
    factorial = 1
    for el in gen_fact(n):
        factorial *= el
    return factorial

# Выдать факториалы чисел от 1 до n
fact_num = 6
for i in range(1, fact_num + 1):
    print(f'{i}! = {fact(i)}')
