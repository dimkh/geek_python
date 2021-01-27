# Модуль описания класса "Склад"
import my_except as me
import office_equipment as off_eq


class Storage:

    MAX_UNITS = 50   # Максимальное количество единиц техники для хранения
    count_units = 0  # Текущее количество единиц техники на складе
    type_units = {}  # Список типов оборудования на складе и количество
    units_list = []  # Список оборудования на складе

    @classmethod
    def add_units(cls, units: off_eq.OfficeEquipment, count: int):
        """ Добавление оборудования на склад.
        На входе: тип и модель техники и количество единиц.
        """
        if Storage.count_units + count > Storage.MAX_UNITS:         # Не можем принять партию - нет мест
            raise me.StorageError("\nБольшая партия - нет мест! Возврат...")
        else:
            Storage.count_units += count

        if units.name not in Storage.type_units:      # Поступил новый тип оборудования
            Storage.type_units[units.name] = count
        else:
            Storage.type_units[units.name] += count   # Учитываем количество

        for i in Storage.units_list:
            if i[0] == units.model:          # Такая модель уже есть на складе добавляем количество
                i[2] += count
                break
        else:
            Storage.units_list.append([units.model, units.name, count])

    @classmethod
    def get_type_units(cls) -> str:
        """ Возвращает список типов оборудования на складе и их количество одной строкой
        """
        result = ''
        count = 0
        for key in Storage.type_units:
            result = f'{result}{key} - {Storage.type_units[key]}\n'
            count += Storage.type_units[key]
        if result:
            return f'\nНа складе имеется:\n{result}ИТОГО: {count} ед.\n'
        else:
            return '\nСклад пуст!'

    @classmethod
    def choice_type(cls) -> str:
        """ Выбор типа оборудования (из существующих)
        На выходе: тип или пустая строка, если ничего не выбрал
        """
        num = 1
        temp_dict = {0: ''}
        result = ''
        print('\n0 - Выход в главное меню')
        for key in Storage.type_units:
            temp_dict[num] = key
            print(f'{num} - {temp_dict[num]}')
            num += 1
        while True:
            choice = input('Что именно интересует? ')
            if choice.isdigit():
                choice = int(choice)
            else:
                break
            if 0 <= choice < num:
                result = temp_dict[int(choice)]
                break
        return result

    @classmethod
    def get_models(cls, type_name: str) -> str:
        """ Возвращает список моделей конкретного типа техники с их количеством
        На входе: тип оборудования
        На выходе: список имеющихся моделей на складе
        """
        result = '\n'
        for el in Storage.units_list:
            if el[1] == type_name:
                result = f'{result}{el[0]} - {el[2]} ед.\n'
        return result

    @classmethod
    def remove_model(cls, model: str, count: int) -> int:
        """ Перемещение техники со склада
        На входе: модель техники и количество
        На выходе: сколько единиц перемещено
        """
        result = 0
        for el in Storage.units_list:
            if el[0] == model:          # Нашли нужную модель
                if count <= el[2]:      # Корректируем количество единиц
                    el[2] -= count
                    Storage.count_units -= count
                    Storage.type_units[el[1]] -= count
                    result = count
                else:
                    raise me.StorageError('Столько на складе нет!')
                break
        return result

    @classmethod
    def choice_model(cls, type_name: str) -> str:
        """ Выбор модели конкретного типа техники.
        На входе: тип оборудования
        На выходе: выбранная модель
        """
        num = 1
        temp_dict = {0: ''}
        print('\n0 - Выход без выбора')
        for el in Storage.units_list:
            if el[1] == type_name:
                temp_dict[num] = el[0]
                print(f'{num} - {temp_dict[num]}')
                num += 1
        while True:
            choice = input('Что именно интересует? ')
            if choice.isdigit() and 0 <= int(choice) < num:
                result = temp_dict[int(choice)]
                break
        return result
