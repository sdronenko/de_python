# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = list(input('Введите числа: ').split())
i = 0
print(f'Ваш список: {my_list}')
while i + 1 < len(my_list):
    if i % 2 == 0:
        my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
    i += 1
print(f'Лист: {my_list}')

# el_count = int(input("Введите количество элементов списка: "))
# my_list = []
# i = 0
# el = 0
# while i < el_count:
#     my_list.append(input("Введите значение: "))
#     i += 1
#
# for elem in range(int(len(my_list)/2)):
#         my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
#         el += 2
# print(my_list)

# my_list = list(input('Введите числа: ').split())
# i = 0
# print(f'Ваш список: {my_list}')
# while i + 1 < len(my_list):
#     if i % 2 == 0:
#         el = my_list.pop(i + 1)
#         my_list.insert(i, el)
#     i += 1
# print(f'Лист: {my_list}')
