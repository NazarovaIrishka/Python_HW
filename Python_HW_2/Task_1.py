# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


N = input('Введите число:')
summa = 0
for s in N:
    if s.isdigit():
        summa += int(s)

print(summa)



num = input('Введите вещественное число: ')
sum = 0
for i in num:
    if i != '.' and i != '-' and i != ',':
        sum += int(i)
print(sum)



numb = float(input())
summ = 0
for el in str(numb):
    if el != '.':
        summ += int(el)
print(summ)


n = float(input('Введите число - '))
while n % 1 > 0:
    n *= 10
    summ = 0
while n > 0:
    summ += n % 10
    n //= 10
print(int(summ))

