# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

#          Было
# N = input('Введите число:')
# summa = 0
# for s in N:
#     if s.isdigit():
#         summa += int(s)

# print(summa)

#          Стало
N = input('Введите число:')
S = sum (map(int, filter(lambda n: n.isdigit(), N )))
print(S)