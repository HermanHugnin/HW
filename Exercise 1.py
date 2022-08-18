from random import random, randint, randrange, choice
from itertools import count, cycle
from functools import reduce
from time import time

# Задача 1
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

def salary(x, y, z):
    return x * y + z
hours_worked = int(input('Введите количество отработанных часов работника: '))
hours = int(input('Введите ставку работника за час: '))
bonus = int(input('Введите премию работника: '))
your_salary = salary(hours_worked, hours, bonus)
print(your_salary)
