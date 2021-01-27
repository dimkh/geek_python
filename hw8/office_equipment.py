# Модуль с описанием классов офисной техники
class OfficeEquipment:

    def __init__(self, name: str, model: str, resolution: int, format_page: str, speed: int):
        self.name = name                    # Название устройства
        self.model = model                  # Модель устройства
        self.resolution = resolution        # Разрешение устройства (точек на дюйм)
        self.format_page = format_page      # Максимальный формат бумаги (А4, А3 и т.п.)
        self.speed = speed                  # Скорость работы (страниц в минуту)
        self.department = 'storage'         # Текущее место расположения устройства


class Printer(OfficeEquipment):

    def __init__(self, name: str, model: str, resolution: int, format_page: str, speed: int,
                 type_eq: str, color: bool, both_sides: bool, connection: str):
        super().__init__(name, model, resolution, format_page, speed)
        self.type_eq = type_eq              # Тип принтера (лазерный, струйный)
        self.color = color                  # Цветной или черно-белый
        self.both_sides = both_sides        # Двусторонняя печать
        self.connection = connection        # Подключение (сеть, комп)


class Scanner(OfficeEquipment):

    def __init__(self, name: str, model: str, resolution: int, format_page: str, speed: int,
                 auto_feed: bool, both_sides: bool, connection: str):
        super().__init__(name, model, resolution, format_page, speed)
        self.auto_feed = auto_feed          # Автоподача (есть, нет)
        self.both_sides = both_sides        # Двустороннее сканирование
        self.connection = connection        # Подключение (сеть, комп)


class Copier(OfficeEquipment):

    def __init__(self, name: str, model: str, resolution: int, format_page: str, speed: int,
                 copies_per_cycle: int):
        super().__init__(name, model, resolution, format_page, speed)
        self.copies_per_cycle = copies_per_cycle    # Max копий за цикл
