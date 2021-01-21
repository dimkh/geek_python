from abc import ABC, abstractclassmethod


class Clothes(ABC):

    def __init__(self, size: int, title: str):
        self._size = size        # Размер вещи
        self.title = title       # Название вещи

    @abstractclassmethod
    def get_material(self) -> float:
        """ Возвращает расход ткани для пошива одежды
        """
        pass


class Coat(Clothes):

    def __init__(self, size: int, title="Пальто"):
        super().__init__(size, title)

    @property
    def get_material(self) -> float:
        """ Возвращает расход ткани для пошива пальто
        """
        return self._size / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, size: int, title="Костюм"):
        super().__init__(size, title)

    @property
    def get_material(self) -> float:
        """ Возвращает расход ткани для пошива костюма
        """
        return self._size * 2 + 0.3


my_coat = Coat(6, "Реглан")
print(f'\nРасход ткани на пошив пальто: {my_coat.title} - {my_coat.get_material:.2f} кв.м.')

my_suit1 = Suit(2, "Фрак")
my_suit2 = Suit(2, "Тройка")
print(f'Расход ткани на пошив костюма: {my_suit1.title} - {my_suit1.get_material:.2f} кв.м.')
print(f'Расход ткани на пошив костюма: {my_suit2.title} - {my_suit2.get_material:.2f} кв.м.')

print(f'Общий расход ткани: {my_coat.get_material + my_suit1.get_material + my_suit2.get_material:.2f} кв.м.')
