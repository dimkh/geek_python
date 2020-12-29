def user_per_row(user_surname, user_name, user_birthday_year,
                 user_phone, user_city, user_email):
    """ Возвращает данные пользователя одной строкой.
    На входе: имя пользователя, фамилия, год рождения, город проживания,
              email, телефон (именованные аргументы).
              Проверка входных данных не производится.
    На выходе: данные пользователя одной строкой.

    """
    return f'{user_name} {user_surname} {user_birthday_year} '\
           f'{user_city} {user_email} {user_phone}'

u_name = "Василий"
u_surname = "Сидоров"
u_birthday_year = 1985
u_city = "Екатеринбург"
u_email = "vasya.sidorov@gmail.com"
u_phone = "+79123456789"

print()
print(user_per_row(user_surname = u_surname, user_name = u_name,
      user_birthday_year = u_birthday_year, user_phone = u_phone,
      user_city = u_city, user_email = u_email))