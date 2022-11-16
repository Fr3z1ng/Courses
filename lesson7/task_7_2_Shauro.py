"""
2. Создайте лямбда выражение, которое из входного списка из строк произведет фильтрацию и оставит только те элементы,
которые являются палиндромами и результат вернет в виде кортежа, например («rotator», «noon»)
"""
list_1 = ["Rotator", "Noon", "abf"]
list_2 = []
for item in list_1:
    item = item.lower()
    list_2.append(item)
a = list(filter(lambda x: x == x[::-1], list_2))
print(a)
