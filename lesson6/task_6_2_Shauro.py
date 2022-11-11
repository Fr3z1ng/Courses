"""
2. Создайте функцию которая получает в качестве аргумента произвольную строку
и заменяет все символы " на ' и наоборот
"""

s = input("Введите строку:")


def func_replace(s: str) -> str:
    """
    заменяет все символы " на ' и наоборот
    """
    z = []
    for i in s:
        if '"' in i:
            z.append(i.replace('"', "'"))
        else:
            z.append(i.replace("'", '"'))
    return " ".join(z)


if __name__ == '__main__':
    print(func_replace(s))
