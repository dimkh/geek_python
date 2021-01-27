class ElementIsString(Exception):

    def __init__(self, txt):
        self.txt = txt


def str2digit(el: str) -> int:
    """ Конвертирование строки в число
    На входе: строка
    На выходе: число
    """
    if not el.isdigit():
        raise ElementIsString('Ошибка! Введено не число.')

    return int(el)


numbers_list = []
print('Формирование списка чисел. Для окончания введите "stop"')
while True:
    elem = input('Введите элемент списка: ')
    if elem == 'stop':
        break
    try:
        numbers_list.append(str2digit(elem))
    except ElementIsString as err:
        print(err)

print(f'Итоговый список: {numbers_list}')
