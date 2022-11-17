"""
4. Создайте декоратор log_function, который будет выполнять вывод в консоль информации о декорированной функии,
 в частности — время вызова, имя функции, информацию о типах аргументов, которые ожидаются для передачи в функцию,
переданные аргументы (переданные по позиции и по ключевому слову), например

@ log_function
def test(a:int, b:str):
       print(a, b)

test(1, 'time')

Вывод: 2022-11-16 08:44:42.290025 | Function: test | Expected: {'a': <class 'int'>, 'b': <class 'str'>} | Input: (1, 'time')

"""
import time


def log_function(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        name = result.__name__
        annotations = result.__annotations__



a = 5
b = 3


def sasha(a:int, b:int):
    print(sasha.__doc__)
    print(sasha.__annotations__)
sasha(a,b)