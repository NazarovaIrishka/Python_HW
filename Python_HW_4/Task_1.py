#Задача 1. Вычислить число c заданной точностью d.

import math
d = input('Введите число до которого будет округдено число pi ')
d = d[2:len(d)]
print(round(math.pi,len(d)))


