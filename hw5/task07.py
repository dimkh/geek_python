import json


file_name = 'companies.txt'
output_file = 'companies.json'
companies = []
profit_firms = {}
loss_firms = {}
average_profit = {}
avg_profit = 0
result_list = []

# Читаем информацию по компаниям из файла
try:
    with open(file_name, 'r', encoding='utf-8') as f_obj:
        company = f_obj.readline()
        while company:
            companies.append(company.rstrip('\n'))
            company = f_obj.readline()
except IOError:
    print('Внимание! Ошибка ввода-вывода при чтении файла!')

# Обрабатываем компании
# Формируем списки прибыльных и убыточных компаний
for company in companies:
    firm = company.split()
    profit = int(firm[2]) - int(firm[3])
    if profit >= 0:
        profit_firms[firm[0]] = profit
        avg_profit += profit
    else:
        loss_firms[firm[0]] = profit
average_profit['average_profit'] = int(avg_profit / len(profit_firms))

# Собираем итоговый список
result_list.append(profit_firms)
result_list.append(average_profit)
result_list.append(loss_firms)

# Вывод итогового списка в json-файл
try:
    with open(output_file, 'w', encoding='utf-8') as f_obj:
        json.dump(result_list, f_obj, ensure_ascii=False)
except IOError:
    print('Внимание! Ошибка ввода-вывода при записи файла!')
