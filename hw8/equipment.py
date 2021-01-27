# Формирование первоначального списка оборудования для "загрузки" на склад
# Список в формате "json"
# Для проверки работы проекта этот файл не нужен

import json

FILE_PRINTERS = "printers.json"
FILE_SCANNERS = "scanners.json"
FILE_COPIERS = "copiers.json"

one_unit = {
    "name": "Printer",
    "model": "HP Laser 107a",
    "resolution": 1200,
    "format_page": "A4",
    "speed": 20,
    "department": "shop",
    "type_eq": "Лазерный",
    "color": False,
    "both_sides": False,
    "connection": "USB"
}

one_unit2 = {
    "name": "Printer",
    "model": "Brother HL-1223WR",
    "resolution": 2400,
    "format_page": "A4",
    "speed": 20,
    "department": "shop",
    "type_eq": "Лазерный",
    "color": False,
    "both_sides": False,
    "connection": "Wi-Fi"
}

one_unit3 = {
    "name": "Printer",
    "model": "Canon PIXMA G1416",
    "resolution": 4800,
    "format_page": "A4",
    "speed": 5,
    "department": "shop",
    "type_eq": "Струйный",
    "color": True,
    "both_sides": False,
    "connection": "USB"
}

units = list()
units.append(one_unit)
units.append(one_unit2)
units.append(one_unit3)

with open(FILE_PRINTERS, "a", encoding='utf-8') as write_f:
    json.dump(units, write_f, ensure_ascii=False)

one_unit = {
    "name": "Scanner",
    "model": "Canon CanoScan LiDE 400",
    "resolution": 4800,
    "format_page": "A4",
    "speed": 7,
    "department": "shop",
    "auto_feed": False,
    "both_sides": False,
    "connection": "USB"
}

one_unit2 = {
    "name": "Scanner",
    "model": "Plustek OpticSlim 2610 Plus",
    "resolution": 1200,
    "format_page": "A4",
    "speed": 4,
    "department": "shop",
    "auto_feed": False,
    "both_sides": False,
    "connection": "USB"
}

one_unit3 = {
    "name": "Scanner",
    "model": "Avision FB10",
    "resolution": 600,
    "format_page": "A4",
    "speed": 6,
    "department": "shop",
    "auto_feed": False,
    "both_sides": False,
    "connection": "USB"
}

units = list()
units.append(one_unit)
units.append(one_unit2)
units.append(one_unit3)

with open(FILE_SCANNERS, "a", encoding='utf-8') as write_f:
    json.dump(units, write_f, ensure_ascii=False)

one_unit = {
    "name": "Copier",
    "model": "Kyocera ECOSYS M2040dn",
    "resolution": 1200,
    "format_page": "A4",
    "speed": 40,
    "department": "shop",
    "copies_per_cycle": 999
}

one_unit2 = {
    "name": "Copier",
    "model": "Brother DCP-L2500DR",
    "resolution": 600,
    "format_page": "A4",
    "speed": 26,
    "department": "shop",
    "copies_per_cycle": 99
}

units = list()
units.append(one_unit)
units.append(one_unit2)

with open(FILE_COPIERS, "a", encoding='utf-8') as write_f:
    json.dump(units, write_f, ensure_ascii=False)
