item_template = tuple(("Название", "Цена", "Количество", "Ед.измерения"))
item_list = []

# Формирование структуры данных "Товары"
print('\nВведите информацию о товаре')
print('(для окончания ввода в номере товара введите не число):')
while True:
    item_num = input('\nНомер товара: ')
    if not item_num.isdigit():
        break
    item_name = input(f'{item_template[0]}: ')
    item_price = input(f'{item_template[1]}: ')
    item_count = input(f'{item_template[2]}: ')
    item_measure = input(f'{item_template[3]}: ')

    item_tuple = tuple((item_name, item_price, item_count, item_measure))
    item_list.append([item_num, item_tuple])

# Сбор аналитики
# Список характеристик (количество - из шаблона)
attr_item = [[] for i in range(len(item_template))]
for item in item_list:
    for i in range(len(item_template)):
        attr_item[i].append(item[1][i])

# Формируем итоговый словарь
print('\n')
result_dict = {}
for i in range(len(item_template)):
    result_dict[item_template[i]] = list(set(attr_item[i]))
    print(f'"{item_template[i]}": {result_dict[item_template[i]]}')
print()