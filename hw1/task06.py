current_distance = float(input('\nВведите результат первого дня (км): '))
end_distance = float(input('Введите цель (км): '))

current_day = 1
print('\nРезультат:\n')

while current_distance < end_distance:
    print(f'{current_day}-й день: {current_distance:.2f}')
    current_day += 1
    current_distance *= 1.1
print(f'{current_day}-й день: {current_distance:.2f}')

print(f'\nОтвет: на {current_day}-й день спортсмен достиг результата - не менее {end_distance} км.\n')