# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные, выведите на экран.

a = 20
b = 5.1
c = True
print(a)
print(b)
print(c)
print(a, b, c)
print(type(a))

name = input('Введите Ваше имя: ')
age = int(input('Сколько Вам лет? '))
string = input('Ваша профессия? ')
number = int(input('Введите любое число: '))
print('Добрый день, %s! Вам %d лет. Вы %s. Вы ввели число %d.' % (name, age, string, number))