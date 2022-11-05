a = int(input("Введите число: "))


def sum_number(a: int) -> int:  # решение 1
    """
    функция считает сумму чисел при помощи рекурсии
    """
    suma = 0
    if a // 10 == 0:
        return a
    else:
        digit = a % 10
        suma += digit + sum_number(a // 10)
    return suma


def sum_number_second(a: int) -> int:  # решение 2
    """
    Подсчет каждой цифры в числе через цикл while
    """
    summa = 0
    while a % 10 != 0:
        digit = a % 10
        a = a // 10
        summa += digit
    return summa
