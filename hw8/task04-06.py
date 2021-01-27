import my_except as me
import load_equipment as le
import office_equipment as off_eq
import storage
import other_func as fun

store = storage.Storage()   # Объект класса "Склад оргтехники"
eq_list = []                # Список со всем оборудованием компании
departments = ['storage', 'accounting', 'soft development', 'support']      # Отделы компании

# Чтение списков сохранённой ранее техники
new_prn_list = le.load_printers()           # Список моделей принтеров
new_scn_list = le.load_scanners()           # Список моделей сканеров
new_copy_list = le.load_copiers()           # Список моделей ксероксов


def get_model(eq_lst: list) -> off_eq.OfficeEquipment:
    """ Возвращает новый объект выбранной модели из списка
    На входе: список моделей принтеров/сканеров/ксероксов компании
    На выходе: новый объект выбранной модели из списка либо пустая строка (не выбрал)
    """
    print('\n0 - Выход без выбора')
    num = 1
    nw_eq = ''
    for eq in eq_lst:
        print(f'{num} - {eq["model"]}')
        num += 1
    m_choice = input('Выберите модель: ')
    if m_choice.isdigit() and 0 < int(m_choice) < num:
        eq = eq_lst[int(m_choice) - 1]
        if eq["name"] == "Printer":
            nw_eq = off_eq.Printer(eq["name"], eq["model"], eq["resolution"], eq["format_page"],
                                   eq["speed"], eq["type_eq"], eq["color"], eq["both_sides"],
                                   eq["connection"])
        elif eq["name"] == "Scanner":
            nw_eq = off_eq.Scanner(eq["name"], eq["model"], eq["resolution"], eq["format_page"],
                                   eq["speed"], eq["auto_feed"], eq["both_sides"],
                                   eq["connection"])
        elif eq["name"] == "Copier":
            nw_eq = off_eq.Copier(eq["name"], eq["model"], eq["resolution"], eq["format_page"],
                                  eq["speed"], eq["copies_per_cycle"])
    return nw_eq


def remove_units(model: str, count: int, department_from: str, department_to: str) -> int:
    """ Перемещение техники в другой отдел.
    На входе: модель, количество и отделы (откуда и куда)
    На выходе: количество перемещённых единиц
    """
    result = 0
    for eq in eq_list:
        if eq.model == model and eq.department == department_from:
            eq.department = department_to
            result += 1
            if result == count:
                break
    return result


# Создаём по 5 моделей принтеров и помещаем их на склад
for el in new_prn_list:
    new_eq = off_eq.Printer(el["name"], el["model"], el["resolution"], el["format_page"],
                            el["speed"], el["type_eq"], el["color"], el["both_sides"],
                            el["connection"])
    store.add_units(new_eq, 5)
    for j in range(5):
        eq_list.append(new_eq)
# Аналогично - сканеров
for el in new_scn_list:
    new_eq = off_eq.Scanner(el["name"], el["model"], el["resolution"], el["format_page"],
                            el["speed"], el["auto_feed"], el["both_sides"], el["connection"])
    store.add_units(new_eq, 5)
    for j in range(5):
        eq_list.append(new_eq)
# Аналогично - ксероксов
for el in new_copy_list:
    new_eq = off_eq.Copier(el["name"], el["model"], el["resolution"], el["format_page"],
                           el["speed"], el["copies_per_cycle"])
    store.add_units(new_eq, 5)
    for j in range(5):
        eq_list.append(new_eq)

# Меню программы
while True:
    print('\nГЛАВНОЕ МЕНЮ:')
    print('1 - Что есть на складе? Просмотр типов')
    print('2 - Какие модели? Проверить')
    print('3 - Добавить на склад (новое)')
    print('4 - Выдача оборудования со склада')
    print('0 - Выход')
    choice = input('Ваш выбор: ')
    if choice == '0':
        break
    elif choice == '1':         # Просмотр типов оборудования
        print(store.get_type_units(), end='')
    elif choice == '2':         # Вывод всех моделей
        my_type_eq = store.choice_type()
        if my_type_eq:
            print(store.get_models(my_type_eq))
    elif choice == '3' or choice == '4':         # Добавление или перемещение техники
        my_type_eq = store.choice_type()
        if my_type_eq:
            new_eq = ''
            if my_type_eq == "Printer":
                new_eq = get_model(new_prn_list)
            elif my_type_eq == "Scanner":
                new_eq = get_model(new_scn_list)
            elif my_type_eq == "Copier":
                new_eq = get_model(new_copy_list)
            if new_eq:
                try:
                    new_eq_count = fun.is_digit((input('Сколько единиц техники переместить? ')))
                    if choice == '3':           # Добавляем технику на склад
                        store.add_units(new_eq, new_eq_count)
                        for j in range(new_eq_count):
                            eq_list.append(new_eq)
                    else:                        # Перемещаем технику в отдел
                        new_eq_count = store.remove_model(new_eq.model, new_eq_count)
                        department = fun.choice_department()
                        if new_eq_count:         # На складе удалили, фиксируем новый отдел в списке оборудования
                            remove_units(new_eq.model, new_eq_count, 'storage', department)
                except me.StorageError as err:
                    print(err)
