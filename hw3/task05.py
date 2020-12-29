symb_exit = ''
result = 0
print('\nСуммирование чисел, введённых через пробел.')
print('Enter - завершение ввода порции чисел, q - выход.')

# Организуем цикл, для выхода ввести q
while symb_exit != 'q':
    str_num = input('\nВведите строку чисел: ')
    lst_num = str_num.split()

    # Контроль последнего введённого символа (для выхода)
    symb_exit = lst_num[-1]
    if symb_exit == 'q':
        del lst_num[-1]

    # Переводим список чисел из символов в числа и суммируем
    result += sum([float(elem) for elem in lst_num])

    print(f'Итоговая сумма равна: {result}')