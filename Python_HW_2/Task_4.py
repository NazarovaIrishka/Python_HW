# Реализуйте алгоритм перемешивания списка.

list = [1, 2, 3, 4, 5]
from random import randint

for i in range(len(list)):
    swap = randint(0,len(list)-1)
    temp = list[swap]
    list[swap] = list[i]
    list[i] = temp
print(list)



