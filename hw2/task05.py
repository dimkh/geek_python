my_list = [7, 5, 3, 3, 2]
new_elem = int(input('\nВведите новый элемент рейтинга: '))

my_list.append(new_elem)
my_list.sort(reverse=True)

print(f'Результат: {my_list}')