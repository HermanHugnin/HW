from random import random, randint, randrange, choice
from itertools import count, cycle
from functools import reduce
from time import time

# Задача 5
# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

print(reduce(lambda x, y: x * y, [i for i in [k for k in range(100, 1001) if k % 2 == 0]]))
