def seek_numbers(symbols: str) -> list:
    """ Возвращает список чисел, найденных в строке.
    На входе: строка символов.
    На выходе: список найденных чисел или пустой список, если чисел нет.
    """
    result = []
    num = ''

    for char in symbols:
        if char.isdigit():
            num = f'{num}{char}'
        else:
            if num:
                result.append(int(num))
                num = ''
    if num:                             # Если строка оканчивается цифрой - не теряем последнее число
        result.append(int(num))

    return result


file_name = 'subjects.txt'
subj_dict = {}
one_subj = []

try:
    with open(file_name, 'r', encoding='utf-8') as f_obj:
        subjects = f_obj.readlines()
except IOError:
    print('Внимание! Ошибка ввода-вывода при чтении файла!')

for subj in subjects:
    one_subj = subj.split(':')
    subj_dict[one_subj[0]] = sum(seek_numbers(one_subj[1]))

print('\nУчебная нагрузка:')
print(subj_dict)
