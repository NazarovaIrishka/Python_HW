# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#       Было:

# N = int(input('Введите число:'))
# n= 1
# my_list = list('n = (1 + 1/n)**n')
# print(my_list)
# n= 1
# summa = 0
# for i in range(1, N + 1):
#     n = (1 + 1/n)**n
#     print(n)
#     summa = summa + n
# print(summa)

#       Стало:
N = int(input('Введите число: '))
S = list((1 + 1/n)**n for n in range(1, N + 1))
print(S)
print(f'sum = {round(sum(S))}')

