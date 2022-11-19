"""
*5. Создайте декоратор, remember_result который будет сохраняет результат последнего вызова декорированной
функции и выводить его в консоль перед каждым новым вызовом
@remember_result
def sum_list(*args):
     result = ""
     for item in args:
          result += item
          print(f"Current result = '{result}'")
     return result
sum_list("a", "b")
Last result = 'None'
Current result = 'ab'
sum_list("abc", "cde")
Last result = 'ab'
Current result = 'abccde'
sum_list(3, 4, 5)
Last result = 'abccde'
Current result = '12'
"""
import functools

storage = [None] # переменная для временного хранения памяти


def remember_result(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global storage # для того что бы использовать переменную памяти
        print(f"Last result = {storage}") # показываем результат предыдущей функции
        storage = func(*args, **kwargs) # записывает последний результат для временного хранения

    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        if isinstance(item, int): # проверка валидации является ли аргумент целым числом
            result = list(result) # превращаем result в список что бы лучше посчитать сумму чисел с помощью метода sum()
            result.append(item) # добавляем аргументы в список #
        else:
            result += item # если элемент не является целым числом,то просто добавляем его в строку
    if isinstance(result, list): # если наша переменная является списком,то выводим сумму цифр
        result = sum(result)
        print(f"Current result = '{result}'")
        return result
    else: # если переменная не является списком выводим,строку
        print(f"Current result = '{result}'")
        return result
# можно было наверное запариться разобрать вариант когда может поступать и число и строка,но это сложно :)

sum_list("a", "b")
sum_list("c", "d")
sum_list(3, 4, 5)
sum_list(4, 6, 7)
