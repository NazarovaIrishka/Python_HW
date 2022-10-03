# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

#          Было
# list_1 = [int(i) for i in input('Введите числа: ').split()]
# list_2 = []
# for i in range((len(list_1)+1)//2):
#     list_2.append(list_1[i] * list_1[len(list_1)-1-i])
# print(list_2)

#          Стало
from math import ceil
list_1 = [int(i) for i in input('Введите числа: ').split()]
print(list(list_1[i] * list_1[-i-1] for i in range(ceil(len(list_1)/2))))