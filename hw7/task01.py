class Matrix:

    def __init__(self, init_list: list):
        self._matrix_list = init_list       # Матрица (список списков)
        self._rows = len(init_list)         # Количество строк в матрице
        self._columns = len(init_list[0])   # Количество столбцов

    def __str__(self):
        result = ''
        for row in self._matrix_list:
            for el in row:
                result = f'{result}{str(el):5}'
            result = f'{result}\n'
        return result

    def __add__(self, other):
        result = []

        # При сложении матрицы должны быть одного размера. Разные - возвращаем пустую
        if self._rows != other._rows or self._columns != other._columns:
            return Matrix(result)
        for i in range(self._rows):
            res_row = []
            for j in range(self._columns):
                res_row.append(self._matrix_list[i][j] + other._matrix_list[i][j])
            result.append(res_row)
        return Matrix(result)


print('Матрица 1:')
m1 = Matrix([[1, 2, 3], [4, 5, 6]])
print(m1)
print('Матрица 2:')
m2 = Matrix([[3, 2, 1], [6, 5, 4]])
print(m2)
print('Сумма матриц 1 и 2:')
m = m1 + m2
print(m)
