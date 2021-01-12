from random import randint

file_name = 'numbers4sum.txt'
count_numbers = 10
low_number = 1
high_number = 20

str_numbers = ''
summa = 0

# Генерируем строку чисел по заданным условиям
for i in range(count_numbers):
    str_numbers += f'{randint(low_number, high_number)} '

print('\nСгенерирована строка чисел:')
print(f'{str_numbers}')

# Записываем строку в файл
try:
    with open(file_name, 'w', encoding='utf-8') as f_obj:
        f_obj.write(str_numbers)
except IOError:
    print('Внимание! Ошибка ввода-вывода при записи файла!')

# Считываем строку чисел из файла
try:
    with open(file_name, 'r', encoding='utf-8') as f_obj:
        str_numbers = f_obj.readlines()
except IOError:
    print('Внимание! Ошибка ввода-вывода при чтении файла!')

# Вычисляем сумму чисел
numbers_list = str(str_numbers[0]).split()
for num in numbers_list:
    summa += int(num)

print(f'\nИтоговая сумма чисел из файла {file_name} равна {summa}')
