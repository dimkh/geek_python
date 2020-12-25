season_list = ['Зима', 'Весна', 'Лето', 'Осень', 'Неизвестный календарь']
season_dict = {
    1:  "Зима",
    2:  "Зима",
    3:  "Весна",
    4:  "Весна",
    5:  "Весна",
    6:  "Лето",
    7:  "Лето",
    8:  "Лето",
    9:  "Осень",
    10: "Осень",
    11: "Осень",
    12: "Зима"
}

num_month = int(input('\nВведите номер месяца: '))
if num_month in (1, 2, 12):
    num_season = 0
elif num_month >= 3 and num_month <= 5:
    num_season = 1
elif num_month >= 6 and num_month <= 8:
    num_season = 2
elif num_month >= 9 and num_month <= 11:
    num_season = 3
else:
    num_season = 4
print(f'\nВремя года из списка: {season_list[num_season]}')

season = season_dict.get(num_month)
if (season is None):
    print('Время года из словаря: Неизвестный календарь')
else:
    print(f'Время года из словаря: {season}')