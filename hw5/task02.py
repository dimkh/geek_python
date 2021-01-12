file_name = 'words.txt'

try:
    with open(file_name, 'r', encoding='utf-8') as f_obj:
        content = f_obj.readlines()
        print(f_obj)
except IOError:
    print('Внимание! Ошибка ввода-вывода!')

print(f'\nВсего в файле {len(content)} строк.\n')
i = 1
for line in content:
    print(f'В {i}-й строке {len(line.split())} слов.')
    i += 1
