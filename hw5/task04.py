file_source = 'numbers_en.txt'
file_destination = 'numbers_ru.txt'
content = []

numbers = {
    'One':      'Один',
    'Two':      'Два',
    'Three':    'Три',
    'Four':     'Четыре'
}

# Читаем файл построчно в список
try:
    with open(file_source, 'r', encoding='utf-8') as f_obj:
        one_str = f_obj.readline()
        while one_str:
            content.append(one_str.rstrip('\n'))
            one_str = f_obj.readline()
except IOError:
    print(f'Внимание! Ошибка ввода-вывода в файле {file_source}!')

# Записываем переведённый блок
try:
    with open(file_destination, 'w', encoding='utf-8') as f_obj:
        for line in content:
            number = line.split('-')
            print(f'{numbers.get(number[0].strip(), "Unknown")} - {number[1].strip()}', file=f_obj)
except IOError:
    print(f'Внимание! Ошибка ввода-вывода в файле {file_destination}!')
