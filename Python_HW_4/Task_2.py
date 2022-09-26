# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Введите число: '))
lis = []
simple = 2
while N > 1:
    if N % simple == 0:
        lis.append(simple)
        N = N/simple
    else:
        simple += 1
print(lis)
