"""
3. Реализуйте функцию get_digits(num: int) -> tuple, которая возвращает кортеж
цифр заданного целого числа.
Пример:
get_digits(87178291199)
(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
"""
num = int(input("Введите число: "))


def get_digits(num: int) -> tuple:
    """
    функция возращает кортеж цифр из заданного числа
    :param num:
    :return:
    """
    s = str(num)
    new_list = []
    for i in s:
        new_list.append(int(i))

    return tuple(new_list)

if __name__ == '__main__':
    print(get_digits(num))
