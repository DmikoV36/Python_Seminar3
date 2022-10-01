# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import math
from random import randint
try:
    n = int(input("Введите количество элементов: "))
    random_array = [randint(1, 9) for i in range(n)]
    print(random_array)
    mult_array = [None for _ in range(math.ceil(n/2))]
    def fill_mult_array(array):
        for i in range(math.ceil(n/2)):
            mult_array[i] = random_array[i]*random_array[-(i+1)]
        return mult_array
    print(f"Произведение пар элементов: {fill_mult_array(random_array)}")
except:
    print("Нужно вводить число!")
