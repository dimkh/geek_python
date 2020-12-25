# Различные типы данных Python

my_list = [1, 2.5, complex(3, 4), 'name', [2, 4], (2, 4), set('it is set'),
          {'k1': 1, 'k2': 2}, True, b'1', bytearray(b'12'), None]

for el in my_list:
    print(type(el))