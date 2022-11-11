"""
5. Реализовать функцию, которая получает изменяемое количество словарей (ключи - буквы, значения - числа) и объединяет их в один словарь.
Значения dict должны быть суммированы в случае идентичных ключей
def combine_dicts(*args):
    ...

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2)
{'a': 300, 'b': 200, 'c': 300}
"""
dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}


def sum_dict(*args: dict):
    combine_dicts = {}
    for key, value in args:
        if key == key:
            [key] = value + value
        print(key, value)


sum_dict(dict_1, dict_2)
