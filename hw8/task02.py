class MyZeroDivision(Exception):

    def __init__(self, txt):
        self.txt = txt


def division(num1: int, num2: int) -> float:
    """ Возвращает частное от деления двух чисел
    На входе: делимое и делитель
    На выходе: частное
    """
    if num2 == 0:
        raise MyZeroDivision("Ошибка! Делитель равен нулю.")

    return num1 / num2


print('Введите пару целых чисел - делимое и делитель через пробел.')
print('Для окончания работы введите один любой символ.')
while True:
    from_user = input('Делимое и делитель: ')
    pair_numbers = from_user.split()
    if len(pair_numbers) == 1:
        break
    try:
        print(division(int(pair_numbers[0]), int(pair_numbers[1])))
    except MyZeroDivision as err:
        print(err)
