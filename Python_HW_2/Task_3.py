# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

N = int(input('Введите цифру:'))
n= 1
summa = 0
for i in range(1, N + 1):
    n = (1 + 1/n)**n
    print(n)
    summa = summa + n
print(summa)


