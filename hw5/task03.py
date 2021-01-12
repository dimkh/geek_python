file_name = 'salary.txt'
employee_count = 0
all_salary = 0.0
limit_salary = 20000

try:
    with open(file_name, 'r', encoding='utf-8') as f_obj:
        content = f_obj.readlines()
except IOError:
    print('Внимание! Ошибка ввода-вывода!')

print(f'\nСотрудники с зарплатой менее {limit_salary} руб.:\n')
for line in content:
    employee = line.split()
    salary = float(employee[1])
    all_salary += salary
    employee_count += 1
    if salary < limit_salary:
        print(f'Сотрудник: {employee[0]} - {salary} руб.')
print(f'\nСредняя зарплата по предприятию: {round(all_salary / employee_count, 2)} руб.')
