# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_data(name, surname, dob, city, email, telephone):
    return ' '.join([name, surname, dob, city, email, telephone])


print(user_data(surname='Dronenko', name='Sofya', dob='1995', city='Moscow', email='mail@mail.ru',
                telephone='8-999-222-99-22'))
