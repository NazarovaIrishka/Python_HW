#Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]

# Задача без улучшения
# unique = []
# for i in range(len(my_list)):
#     if my_list[i] not in my_list[i+1::] and my_list[i] not in my_list[:i-1:]:
#         unique.append(my_list[i])
# print(unique)

# Задача с улучшением
result_1 = list (filter(lambda x: my_list.count(x) == 1, my_list))
print(result_1)
