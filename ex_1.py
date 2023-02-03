# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу.
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.
import random

rows = 3
columns = 20
num = [0] * rows

for index in range(len(num)):
    num[index] = [random.randint(2, 5) for _ in range(columns)]

for el in num:
    print(el)

list_avg = []

for i in range(rows):
    avg = sum(num[i]) / columns
    list_avg.append(avg)
print(f'Cредние оценки по трем группам {list_avg}')

max_value = max(list_avg)
max_index = list_avg.index(max_value)
print(f'Группу {max_index + 1} с наилучшим средним баллом {max_value} ')
