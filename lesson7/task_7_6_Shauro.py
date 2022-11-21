"""
6*. Создать лямбда выражение, которое из входного кортежа произвольных чисел составит список чисел,
которые делятся на 9 (проверку деления на 9 осуществлять по правилу:
«если сумма цифр числа делится на 9, то и само число делится на 9»
"""
from functools import reduce

values = (12, 15, 19, 22, 16, 329, 567)
# summa_list = []
# for i in values:
#     suma = 0
#     while i != 0:
#         digit = i % 10
#         i = i // 10
#         suma += digit
#     summa_list.append(suma)
# zip_list = list(zip(values, summa_list))
# print(summa_list)
# a = list(map(list, zip_list))
list_1 = []
for item in values:
    a = list(map(str, str(item)))
    list_1.append(a)
summa_list = []

