# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год.
# Каждому месяцу соответствует своя строка. Определите самый жаркий и самый холодный 7-дневный промежуток каждого месяца.
# Выведите их даты.
import random


def per_for_month(temp_month, per, month):
    max_temp = 0
    day_max_temp = 1
    min_temp = 100
    day_min_temp = 1

    for day in range(len(temp_month) - per + 1):
        temp_per = temp_month[day:day+per]
        sum_temp_per = sum(temp_per)
        if sum_temp_per > max_temp:
            max_temp = sum_temp_per
            day_max_temp = day
        elif sum_temp_per < min_temp:
            min_temp = sum_temp_per
            day_min_temp = day

    print(
        f'Максимальная температура {round(max_temp/per,1)} была с {day_max_temp+1} по {day_max_temp+per} {month}')
    print(
        f'Минимальная температура {round(min_temp/per,1)} была с {day_min_temp+1} по {day_min_temp+per} {month}')


rows = 5
temp_month = [0] * rows
per = 7


temp_month[0] = [random.randint(5, 21) for _ in range(31)]
temp_month[1] = [random.randint(19, 25) for _ in range(30)]
temp_month[2] = [random.randint(16, 35) for _ in range(31)]
temp_month[3] = [random.randint(12, 25) for _ in range(31)]
temp_month[4] = [random.randint(4, 22) for _ in range(31)]


list_month = ['май', 'июнь', 'июль', 'август', 'сентябрь']
for el in range(len(list_month)):
    per_for_month(temp_month[el], per, list_month[el])
