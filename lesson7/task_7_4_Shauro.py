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
from datetime import datetime
import functools

def log_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(f"{start}| Function: {func.__name__} | Expected: {func.__annotations__} | Input: {args}")
        return result

    return wrapper


@log_function
def test(a: int, b: str):
    print(a, b)


test(1, "time")

