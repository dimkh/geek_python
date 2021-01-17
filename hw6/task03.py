class Worker:

    name = ''
    surname = ''
    position = ''
    _income = {"wage": 0.0, "bonus": 0.0}


class Position(Worker):
    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name            # Имя работника
        self.surname = surname      # Фамилия работника
        self.position = position    # Должность
        self._income = income       # Доход: оклад и премия

    def get_full_name(self) -> str:
        """ Возвращает полное имя сотрудника
        """
        return f'{self.name} {self.surname}'

    def get_total_income(self) -> float:
        """ Возвращает полный доход сотрудника (оклад + премия)
        """
        return self._income["wage"] + self._income["bonus"]


employees = list()
employees.append(Position('Василий', 'Иванов',
                          'Начальник цеха', {"wage": 25300, "bonus": 15000}))
employees.append(Position('Сергей', 'Петров',
                          'Токарь', {"wage": 18800, "bonus": 12000}))
employees.append(Position('Игорь', 'Кузнецов',
                          'Ферезровщик', {"wage": 19500, "bonus": 13000}))

for el in employees:
    print(f'Сотрудник: {el.get_full_name()},  общий доход: {el.get_total_income()} руб')
