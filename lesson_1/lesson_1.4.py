# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

n = abs(int(input("Введите целое положительное число: ")))
max_number = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max_number:
        max_number = n % 10
    if n > 9:
        continue
    else:
        print("Самая большая цифра в Вашем числе: ", max_number)
        break
