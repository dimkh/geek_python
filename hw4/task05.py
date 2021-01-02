from functools import reduce

def mltpl(prev_el: int, el: int) -> int:
    """ Функция для reduce, перемножает 2 эелемента
    На входе: элементы списка
    На выходе: произведение 2-х элементов
    """
    return prev_el * el

# Границы диапазона
# Для проверки работы вместо заданных в условии 100 и 1000 взял 1 и 10
start_num = 1
end_num = 10

# Формируем список чётных чисел из заданного диапазона
lst = [el for el in range(start_num, end_num + 1) if el % 2 == 0]

print(reduce(mltpl, lst))

# Реализация через лямбда-функцию
print(reduce(lambda prev_el, el: prev_el * el, lst ))