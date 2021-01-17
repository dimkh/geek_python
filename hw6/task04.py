class Car:

    def __init__(self):
        self.speed = 0.0         # Скорость автомобиля
        self.color = 'Unknown'   # Цвет автомобиля
        self.name = 'Unknown'    # Марка автомобиля
        self.is_police = False   # Полицейский авомобиль?
        self.direction = 'forward'  # Направление

    def go(self) -> bool:
        """ Возвращает True, если машина поехала и False, если стоит
        """
        return bool(self.speed)

    def stop(self) -> bool:
        """ Возвращает True, если машина остановилась и True, если едет
        """
        return not bool(self.speed)

    def turn(self, direction: str):
        """ Устанавливает направление движения автомобиля
        """
        self.direction = direction

    def show_speed(self) -> float:
        """ Возвращает текущую скорость автомобиля
        """
        return self.speed


class PoliceCar(Car):

    def __init__(self, name: str, color: str):
        super().__init__()
        self.name = name
        self.color = color
        self.is_police = True


class SportCar(Car):

    def __init__(self, name: str, color: str):
        super().__init__()
        self.name = name
        self.color = color


class TownCar(Car):

    def __init__(self, name: str, color: str):
        super().__init__()
        self.name = name
        self.color = color
        self._speed_limit = 60  # Ограничение скорости

    def show_speed(self) -> float:
        """ Возвращает текущую скорость автомобиля.
        Если автомобиль превысил установленное ограничение - сообщаем об этом
        """
        if self.speed > self._speed_limit:
            print(f'Автомобиль {self.name} превысил скорость!!!')

        return self.speed


class WorkCar(Car):

    def __init__(self, name: str, color: str):
        super().__init__()
        self.name = name
        self.color = color
        self._speed_limit = 40  # Ограничение скорости

    def show_speed(self) -> float:
        """ Возвращает текущую скорость автомобиля.
        Если автомобиль превысил установленное ограничение - сообщаем об этом
        """
        if self.speed > self._speed_limit:
            print(f'Автомобиль {self.name} превысил скорость!!!')

        return self.speed


my_police_car = PoliceCar("Ford", "бело-синий")
my_police_car.speed = 90
print(f'Автомобиль {my_police_car.name} класса {type(my_police_car).__name__} ', end='')
print(f'движется со скоростью {my_police_car.show_speed()} км/ч')
my_police_car.turn('left')
print(f'Автомобиль {my_police_car.name} повернул на {my_police_car.direction}')

my_sport_car = SportCar("Porsche", "красный")
print(f'\nАвтомобиль {my_sport_car.name} класса {type(my_sport_car).__name__} ', end='')
print(f'в настоящее время стоит - {my_sport_car.stop()}')
my_sport_car.speed = 100
print(f'Теперь он движется со скоростью {my_sport_car.show_speed()} км/ч')

my_town_car = TownCar("Peugeot", "желтый")
print(f'\nАвтомобиль {my_town_car.name} класса {type(my_town_car).__name__} ', end='')
print(f'в настоящее время движется - {my_town_car.go()}')
my_town_car.speed = 70
print(f'Теперь он движется со скоростью {my_town_car.show_speed()} км/ч')

my_work_car = WorkCar("Renault", "серебристый")
my_work_car.speed = 10
print(f'\nАвтомобиль {my_work_car.name} класса {type(my_work_car).__name__} ', end='')
print(f'в настоящее время движется - {my_work_car.go()}, скорость {my_work_car.show_speed()} км/ч')
my_work_car.speed = 50
print(f'Теперь он движется со скоростью {my_work_car.show_speed()} км/ч')
print(f'Летит, как {my_work_car.color} метеор!!!')
