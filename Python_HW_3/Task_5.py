# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число : '))

negative_fibonacci = [1,-1]
fibonacci = [1,1]

for i in range (2,k):
    list = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(list)
    list_negative = negative_fibonacci[i-2] - negative_fibonacci[i-1]
    negative_fibonacci.append(list_negative)

negative_fibonacci.reverse()
negative_fibonacci.append(0)

print(negative_fibonacci+fibonacci)
