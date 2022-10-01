# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import randint
try:
    n = int(input("Введите количество элементов: "))
    random_array = [randint(1, 9) for i in range(n)]
    print(random_array)
    def sum_odd (list):
        sum = 0
        for i in range(1, n, 2):
            sum = sum + list[i]
        return sum
    print(f"Сумма элементов на нечетных позициях = {sum_odd(random_array)}")
except:
    print("Нужно вводить число!")