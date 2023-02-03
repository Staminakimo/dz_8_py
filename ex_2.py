# Задача 2. Дана квадратная матрица, заполненная случайными числами.
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.
import random

rows = 5
columns = 5
num = [0] * rows

def random_list():
    for index in range(len(num)):
        num[index] = [random.randint(0, 20) for _ in range(columns)]

    for elment in num:
        print(elment)

list_new = []

def sum_list():
    for i in range(rows):
        sum_list_str = sum(num[i])
        list_new.append(sum_list_str)
        print(f'Cумма {i+1} строки = {sum_list_str}')

def dig():
    dig_list = []
    for index_i in range(rows):
        for index_j in range(columns):
            if index_i == index_j:
                dig_list.append(num[index_i][index_j])
    print(f'Диагональ {dig_list}')

    sum_dig = sum(dig_list)
    print(f'Сумма по диагонали = {sum_dig}')

    for el_list in list_new:
        if el_list > sum_dig:

            print(
                f'Число {el_list} из {list_new.index(el_list)+1} больше значения по диагонали {sum_dig}')

random_list()
sum_list()
dig()
