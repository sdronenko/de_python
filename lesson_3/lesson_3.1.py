# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.


def div(*args):
    try:
        arg1 = int(input("Введите число 1: "))
        arg2 = int(input("Введите число 2: "))
        res = arg1 / arg2
    except ZeroDivisionError:
        return "Вы не можете делить на ноль."

    return res


print(f'Результат деления:  {div()}')
