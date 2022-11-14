def factorial(n):
    """
    функция для проверки двойного факториала
    """
    summa = 1
    if n % 2 == 0:
        for i in range(2, n+2, 2):
            summa *= i
        return summa
    else:
        for i in range(1, n+2, 2):
            summa *= i
    return summa


print(factorial(7))
