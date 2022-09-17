# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите число: '))
balance = ''
while num > 0 :
    balance = str(num % 2) + balance
    num = num // 2 
print(balance)
