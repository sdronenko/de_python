# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_dict = {
    1: 'winter',
    2: 'winter',
    3: 'spring',
    4: 'spring',
    5: 'spring',
    6: 'summer',
    7: 'summer',
    8: 'summer',
    9: 'autumn',
    10: 'autumn',
    11: 'autumn',
    12: 'winter'}

seasons_list = [
    'winter',
    'winter',
    'spring',
    'spring',
    'spring',
    'summer',
    'summer',
    'summer',
    'autumn',
    'autumn',
    'autumn',
    'winter']

try:
    month = int(input("Введите номер месяца: "))
    print(f'В словаре месяц {month} это {seasons_dict[month]}')
    print(f'В листе месяц {month} это {seasons_list[month - 1]}')
except ValueError as err:
    print('Такого месяца не существует', err)

# seasons_list = ['winter', 'spring', 'summer', 'autumn']

# month = int(input("Введите номер месяца: "))
# if month ==1 or month == 12 or month == 2:
#     print(seasons_dict.get(1))
#     print(seasons_list[0])
# elif month == 3 or month == 4 or month ==5:
#     print(seasons_dict.get(2))
#     print(seasons_list[1])
# elif month == 6 or month == 7 or month == 8:
#     print(seasons_dict.get(3))
#     print(seasons_list[2])
# elif month == 9 or month == 10 or month == 11:
#     print(seasons_dict.get(4))
#     print(seasons_list[3])
# else:
#     print("Такого месяца не существует")
