# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

#          Было

# N = int(input('Введите число:'))
# num_1 = 1
# for i in range(1, N + 1):
#     num_1 *=i
#     print(num_1)

#          Стало
import math 

N = int(input('Введите число: '))
result = list (math.factorial(n) for n in range(1, N +1))
print(result)