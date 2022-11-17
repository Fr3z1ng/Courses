"""
1. Дан словарь, создать новый словарь, поменяв местами ключ и значение
"""
dict_1 = {"лучший": 123, "великолепный": 321}
# for key, value in dict_1.items(): # первый метод решения
#     dict_2[value] = key
# print(dict_2)
dict_keys = dict_1.keys()
dict_value = dict_1.values()
zipped_list = (zip(dict_value, dict_keys))  # объединяем значения в tuple помощью метода zip
dict_zipped = dict(zipped_list)  # преобразуем объект в словарь
print(dict_zipped)

dict_2 = {value: key for key, value in dict_1.items()}
print(dict_2)
