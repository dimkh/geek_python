from itertools import count
from itertools import cycle

# Генератор целых чисел, начиная с указанного
first_num = 3       # Стартовое число
end_num = 10        # Условие завершения - последнее число последовательности

for el in count(first_num):
    if el > end_num:
        break
    print(el)

print()
# Повторение списка несколько раз
lst = "Repeatable string "      # Список для повторение
count = 3                       # Количество повторений

cnt_stop_symb = len(lst) * count
cnt = 0
for el in cycle(lst):
    if cnt > cnt_stop_symb - 1:
        break
    print(el, end = '')
    cnt += 1