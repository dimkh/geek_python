file_name = 'text.txt'
new_str = 'abc'

print(f'\nВывод введённых строк в файл {file_name}.')
print('Если файл существует - запись в конце, иначе в новый файл.')
print('Для окончания нажмите Enter \n')

try:
    with open(file_name, 'a', encoding='utf-8') as f_obj:
        while new_str:
            new_str = input('? ')
            f_obj.write(f'{new_str}\n')
except IOError:
    print('Внимание! Ошибка ввода-вывода!')
