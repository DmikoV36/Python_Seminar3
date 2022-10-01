# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import uniform
try:
    n = int(input("Введите количество элементов: "))
    random_array = [round(uniform(-9, 9), 3) for i in range(n)]
    print(random_array)
    def dif_frac (list):
        result = 0
        min = 1
        max = 0
        for i in range(n):
            if round(random_array[i]%1, 3) < min:
                min = round(random_array[i]%1, 3)
            if round(random_array[i]%1, 3) > max:
                max = round(random_array[i]%1, 3)
        print(f"Максимальное значение дробной части элементов {max}")
        print(f"Минимальное значение дробной части элементов {min}")
        return round(max - min, 3)
    print(f"Разница между максимальным и миниамльным значением дробной части = {dif_frac(random_array)}")
except:
    print("Нужно вводить число!")