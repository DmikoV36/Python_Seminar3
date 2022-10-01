# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

try:
    n = int(input("Введите десятичное число: "))
    def decimal_to_binary (n):
        decimal_number = n
        num = ""
        while decimal_number > 0:
            num = num + str(decimal_number % 2)
            decimal_number = decimal_number // 2
        binary_number = 0
        for i in range(len(num) - 1, -1, -1):
            binary_number = binary_number * 10 + int(num[i])
        return binary_number
    print(f"ЧИсло {n} в двоичной системе счисления: {decimal_to_binary(n)}")
except:
    print("Нужно вводить целое число!")