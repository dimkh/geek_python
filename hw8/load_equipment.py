# Модуль чтения сохранённого ранее оборудования из файла
# (чтобы не вручную формировать стартовую ситуацию)
import json

FILE_PRINTERS = "printers.json"
FILE_SCANNERS = "scanners.json"
FILE_COPIERS = "copiers.json"

def load_printers() -> list:
    """ Загрузка списка принтеров из файла
    На выходе: список со словарями конкретных моделей принтеров
    """
    with open(FILE_PRINTERS, encoding='utf-8') as read_f:
       data = json.load(read_f)

    return data

def load_scanners() -> list:
    """ Загрузка списка сканеров из файла
    На выходе: список со словарями конкретных моделей сканеров
    """
    with open(FILE_SCANNERS, encoding='utf-8') as read_f:
       data = json.load(read_f)

    return data

def load_copiers() -> list:
    """ Загрузка списка ксероксов из файла
    На выходе: список со словарями конкретных моделей ксероксов
    """
    with open(FILE_COPIERS, encoding='utf-8') as read_f:
       data = json.load(read_f)

    return data
