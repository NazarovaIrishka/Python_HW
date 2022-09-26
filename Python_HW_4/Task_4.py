# Задана натуральная степень k. Сформировать 
# случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

import random
from random import randint

def create_polynomial(k):
    coefs = []
    for i in range(k+1):
        coefs.append(randint(0, 100))
    return coefs

def format_polynomial(coefs):
    output = ""
    for i in range(k, -1, -1):
        c = coefs[i]
        if c != 0: 
            if output != "": 
                output += (" + " if c > 0 else " - ")
            else:
                if c < 0: output += "-"
            if c != 1 and c != -1: 
                output += str(abs(c))
                if i > 0: output += "*"   
            if i > 0: output += ("x" if i == 1 else "x^" + str(i))
    return output

k = int(input("Задайте степень k: "))
coefs = create_polynomial(k)
output = format_polynomial(coefs)
print(coefs)
print(output + " = 0")

with open ('polynomials_1.txt', 'w') as file:
    file.write(output)

# создала второй фаил с другим многочленом.
coefs = create_polynomial(k)
output_2 = format_polynomial(coefs)
print(coefs)
print(output_2 + " = 0")

with open ('polynomials_2.txt', 'w') as file:
    file.write(output_2)



