# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# многочлены создала и взяла из предыдущего задания.

# не смогла решить эту задачу. Посмотрела на семинаре, поняла как она работает. Но выдаёт ошибку.
# File "c:/Users/Serg/Desktop/Python  practic/Python_HW/Python_HW_4/Task_5.py", line 39, in <module>
#     f.write(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
# ValueError: invalid literal for int() with base 10: '+ 4'
# не понимаю как её исправить

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
f.write((int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
print((int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
f.close()
