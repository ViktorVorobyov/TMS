"""Задачу решал в лоб и без оформления. Очень хотелось спать"""

import random

solar = random.randint(1, 1000000)
print(solar)
x = solar
list = []

while solar > 0:
    if solar // x ** 2 == 0:
        x = x - 1
    elif solar // x ** 2 == 1:
        solar = solar - x ** 2
        list.append(x)
print(list)
