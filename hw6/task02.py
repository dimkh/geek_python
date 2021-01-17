class Road:

    def __init__(self, length: int, width: int):
        self._length = length   # длина дороги (в метрах)
        self._width = width     # ширина дороги (в метрах)

    def count_weight(self, weight_per_meter2: int, thickness: int) -> int:
        """ Вычисляет требуемую массу асфальта
        На входе: масса 1 кв. метра асфальта толщиной 1 см, толщина покрытия (в см)
        На выходе: необходимое количество асфальта (в тоннах)
        """
        return int(self._length * self._width * weight_per_meter2 * thickness / 1000)


r = Road(5000, 20)
print(f'Для покрытия дороги необходимо {r.count_weight(25, 5)} тонн асфальта')
