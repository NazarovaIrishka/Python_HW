# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

# изнчально поняла задачу так, что нужно создать вторую последовательность, 
# в которой не будет таких же элементов как в первой последовательности.

# from random import randint

# num = int(input('Введите колличество чисел: '))
# of = int(input('Введите от какого числа: '))
# until = int(input('Введите до какого числа: '))

# list_1 = []
# for i in range(num):
#     list_1.append(randint(of,until))
# print(list_1)

# list_2 = []
# while len(list_2) < len (list_1):
#     n = randint(of, until)
#     if n not in list_1:
#         list_2.append(n)

# print(list_2)

# Посмотрела семинар, поняла, что непрвильно поняла смысл задачи.
# Не стала удалять решение "своей" задачи.

from random import randint
size = int(input('Введите колличество чисел: '))
A = int(input('Введите от какого числа: '))
B = int(input('Введите до какого числа: '))

list_1 = [randint(A, B) for i in range(size)]
list_2 = [i for i in set(list_1)]

print(list_1)
print(list_2)

