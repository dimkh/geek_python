str_n = input('\nВведите какое-нибудь число: ')
str_n2 = f'{str_n}{str_n}'
str_n3 = f'{str_n2}{str_n}'
print(f'Вычисляем сумму: {str_n} + {str_n2} + {str_n3}')
print(f'Итоговая сумма: {int(str_n) + int(str_n2) + int(str_n3)}\n')