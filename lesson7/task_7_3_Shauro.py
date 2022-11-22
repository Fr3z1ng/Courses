"""
3. Реализовать функцию, которая будет работать аналогично функции map,
 без использования map (возвращаемым объектом может быть список)
"""

value_1 = lambda x: x ** 2
list_1 = [1, 3, 5]
list_2 = [4, 5, 6]
from typing import Callable


def mapping(value_1: Callable, *args):
    """
    функция работает как функция map,но с одним аргументом
    """
    new_list = []
    values = args
    for value in values:
        for item in value:
            new_list.append(value_1(item))
        return new_list


print(mapping(value_1, list_1))
