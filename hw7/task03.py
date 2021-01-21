class BigCell:

    def __init__(self, count_cells=0):

        self.count_cells = count_cells      # Количество ячеек в клетке

    def __str__(self):
        return str(self.count_cells)

    def __add__(self, other):
        return BigCell(self.count_cells + other.count_cells)

    def __sub__(self, other):
        if self.count_cells > other.count_cells:
            return BigCell(self.count_cells - other.count_cells)
        else:
            print('Ошибка при вычитании!!! Первая клетка должна быть больше второй!')
            return BigCell(0)

    def __mul__(self, other):
        return BigCell(self.count_cells * other.count_cells)

    def __truediv__(self, other):
        return BigCell(round(self.count_cells / other.count_cells))

    def make_order(self, cells_per_row: int) -> str:
        """ Возвращает строку, в которой ячейки разбиты на несколько рядов.
        На входе: количество ячеек в ряду.
        На выходе: строка из нескольких рядов ячеек клетки.
        """
        rows = self.count_cells % cells_per_row
        rest_cells = self.count_cells // cells_per_row
        one_row = f'{"*" * cells_per_row}\n'

        return f'{one_row * rows}{"*" * rest_cells}'


c1 = BigCell(7)
c2 = BigCell(5)
print(f'\nКоличество ячеек в клетках: {c1.count_cells} и {c2.count_cells}\n')
print(f'Сложение: {c1 + c2}')
print(f'Вычитание: {c1 - c2}')
print(f'Умножение: {c1 * c2}')
print(f'Деление: {c1 / c2}')
print('\nВывод по 6 ячеек из произведения:')
c3 = c1 * c2
print(f'{c3.make_order(6)}')
