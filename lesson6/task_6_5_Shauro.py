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
from collections import Counter

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}


def sum_dict(*args):
    result = args
    answer = {}
    for d in result:
        for key, value in d.items():
            if key in answer:
                answer[key] += value
            else:
                answer[key] = value
    return answer


print(sum_dict(dict_1, dict_2, dict_3))

# def sum_dict(*args: dict):
#     value = [Counter(d) for d in args]
#
#     result = Counter()
#     for d in value:
#         result += d
#     return dict(result)