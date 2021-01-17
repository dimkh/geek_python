from itertools import cycle
from time import sleep


class TrafficLight:

    def __init__(self):
        self._color = ''    # Текущий цвет светофора
        self._timing_lights = (['красный', 7],  # Порядок переключения и тайминг (в сек)
                               ['желтый', 2],
                               ['зеленый', 5])

    def running(self):
        """ Запуск светофора в бесконечный цикл
        """
        for el in cycle(self._timing_lights):
            self._color = el[0]
            print(self._color)
            sleep(el[1])


# Штатное завершение работы программы по условиям задачи не предусмотрено
# (многопоточность пока не проходили)
# Необходима принудительная остановка работы
# P.S. Порядок переключения задан, в проверке не нуждается

t = TrafficLight()
t.running()
