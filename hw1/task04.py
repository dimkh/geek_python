str_num = input('\nВведите целое число: ')
if str_num.isdigit():
    i = 9
    while i >= 0:
        if str(i) in str_num:
            print(f'Максимальная цифра в числе: {i}\n')
            break
        i -= 1
else:
    print('Ошибка при вводе числа!')