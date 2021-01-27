class MyDate:

    cls_day = 0
    cls_month = 0
    cls_year = 0

    def __init__(self, date_str: str):
        self.date_str = date_str

    def set_date(self):
        MyDate.set_date_attr(self.date_str)

    @classmethod
    def set_date_attr(cls, date_str: str):
        """ Извлекает день, месяц и год из даты (строки) в соответствующие атрибуты класса
        На входе: дата в формате 'DD-MM-YYYY'
        """
        date_lst = date_str.split('-')
        if MyDate.date_validate(int(date_lst[0]), int(date_lst[1]), int(date_lst[2])):
            MyDate.cls_day = int(date_lst[0])
            MyDate.cls_month = int(date_lst[1])
            MyDate.cls_year = int(date_lst[2])
        else:
            MyDate.cls_day = 0
            MyDate.cls_month = 0
            MyDate.cls_year = 0
            print('Ошибка в дате!')

    @staticmethod
    def date_validate(day: int, month: int, year: int) -> bool:
        """ Проверка корректности даты
        На входе: день, месяц, год
        На выходе: True, если дата корректная и False, если нет
        """
        days_per_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                          7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        if year < 1900 or year > 2021:
            return False
        if month < 1 or month > 12:
            return False
        days = days_per_month[month]
        if month == 2 and MyDate.is_leap_year(year):
            days = 29
        if day < 1 or day > days:
            return False

        return True

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """ Проверка високосного года
        На входе: год
        На выходе: True, если год високосный и False, если нет
        """
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True

        return False


md1 = MyDate('02-12-2020')
md1.set_date()
print(f'{MyDate.cls_day}-{MyDate.cls_month}-{MyDate.cls_year}')

md2 = MyDate('32-12-2020')
md2.set_date()
