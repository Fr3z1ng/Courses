"""
5*. Реализуйте генератор, который будет бесконечно генерировать числа Фибоначчи (https://en.wikipedia.org/wiki/Fibonacci_number).
"""


def fibonacci():
    """
    Класс генератора который выводит числа фибоначи до бесконечности
    """
    fib_1 = 0
    fib_2 = 1
    while True:
        yield fib_2
        fib_1, fib_2 = fib_2, fib_1 + fib_2


fib = fibonacci()
while True:
    print(next(fib), end=" ")
