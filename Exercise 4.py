from random import random, randint, randrange, choice
from itertools import count, cycle
from functools import reduce
from time import time

# Задача 4
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
b = list(set(a))
x = [k for k in a if not k in b or b.remove(k)]
print([i for i in a if i not in x])
# не понимаю почему, когда я начинаю редуцировать код,подставляя переменные,
# чтобы сделать программу в одну строку, то у меня все ломается