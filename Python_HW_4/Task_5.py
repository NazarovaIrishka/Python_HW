# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# не решила эту задачу. Посмотрела на семинаре, поняла какона работает. Но выдаёт ошибку.
# File "c:/Users/Serg/Desktop/Python  practic/Python_HW/Python_HW_4/Task_5.py", line 39, in <module>
#     f.write(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
# ValueError: invalid literal for int() with base 10: '+ 4'
# не понимаю как её исправить

import random
def nmnogochlen1(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), res='') -> str:
    f = open('polynomials_1.txt', 'w')
    f.write(nmnogochlen1())
    print(nmnogochlen1())
    f.close()
def nmnogochlen2(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), res='') -> str:
    f = open('polynomials_2.txt', 'w')
    f.write(nmnogochlen2())
    print(nmnogochlen2())
    f.close()

f = open('polynomials_1.txt', 'r')
list_5 = str(f.readline()).split('x')
c1 = b1 = a1 = 0
if len(list_5) == 3:
    c1 = list_5[2][1:]
if len(list_5) >= 2:
    b1 = list_5[1][3:-1]
a1 = list_5[0][:-1]
f.close()

f = open('polynomials_2.txt', 'r')
list_51 = str(f.readline()).split('x')
c2 = b2 = a2 = 0
if len(list_51) == 3:
    c2 = list_51[2][1:]
if len(list_51) >= 2:
    b2 = list_51[1][3:-1]
a2 = list_51[0][:-1]
f.close()

f = open('polynomials_sum.txt', 'w')
f.write(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
print(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
f.close()
