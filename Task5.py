# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры), причем чтоб количество элементов было четное. 
# Вывести на экран красивенько таблицей. Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно переместился на другое место
#  и выполнить это за m*n / 2 итераций. То есть если массив три на четыре, то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

from random import randint
try:
    m = int(input("Введите количество строк массива: "))
    n = int(input("Введите количество столбцов массива: "))
    if (m * n) % 2 != 0:
        print("Количество элементов массива должно быть четно!")
        exit()
except:
    print("Нужно вводить числа!")
    exit()

random_array = [[randint(10, 99) for j in range(n)] for i in range(m)]
def print_matrix(matrix):
    for i in range(m): 
        print(random_array[i])
print("Исходный массив:")
print_matrix(random_array)

def sort_array(list):
    list = [i for i in range(m*n)]
    while len(list) > 0:
        temp = 0
        k = list[randint(0, len(list) - 1)]
        temp = random_array[k//n][k%n]
        list.remove(k)
        l = list[randint(0, len(list) - 1)]
        random_array[k//n][k%n] = random_array[l//n][l%n]
        random_array[l//n][l%n] = temp
        list.remove(l)
    return random_array
print("Отсортированный массив:")
print_matrix(sort_array(random_array))
