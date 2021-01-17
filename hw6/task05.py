class Stationary:

    def __init__(self):
        self.title = ''     # Название предмета

    def draw(self):
        """ Отрисовка объекта
        """
        print('Запуск отрисовки.')


class Pen(Stationary):

    def __init__(self):
        super().__init__()
        self.title = 'Ручка'

    def draw(self):
        """ Отрисовка объекта Pen
        """
        print(f'Запуск отрисовки для экземпляра объекта {self.__class__.__name__}')
        print(f'Рисует {self.title.upper()}!')


class Pencil(Stationary):

    def __init__(self):
        super().__init__()
        self.title = 'Карандаш'

    def draw(self):
        """ Отрисовка объекта Pencil
        """
        print(f'\nЗапуск отрисовки для экземпляра объекта {self.__class__.__name__}')
        print(f'Рисует {self.title.upper()}!')


class Handle(Stationary):

    def __init__(self):
        super().__init__()
        self.title = 'Маркер'

    def draw(self):
        """ Отрисовка объекта Handle
        """
        print(f'\nЗапуск отрисовки для экземпляра объекта {self.__class__.__name__}')
        print(f'Рисует {self.title.upper()}!')


my_pen = Pen()
my_pen.draw()

my_pencil = Pencil()
my_pencil.draw()

my_handle = Handle()
my_handle.draw()
