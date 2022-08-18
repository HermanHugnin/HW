from random import random, randint, randrange, choice
from itertools import count, cycle
from functools import reduce
from time import time

# Задача 2
# Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.

data = list(map(int, input().strip().split()))
print([data[i] for i in range(1, len(data)) if data[i] > data[i - 1]])
