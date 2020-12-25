orig_list = list(input('\nВведите элементы списка: '))
print(f'Оригинальный список: {orig_list}')
new_list = []

for i in range(len(orig_list)):
    # Первый элемент - добавляем, второй - вставляем перед первым (и т.д.)
    if (i % 2):
        new_list.insert(i - 1, orig_list[i])
    else:
        new_list.append(orig_list[i])
print(f'Новый список:        {new_list}')
# Ликвидируем оригинальный список
orig_list = new_list