"""
4*. Реализуйте класс итератора EvenRange, который принимает начало и конец интервала в качестве аргументов инициализации и выдает только четные числа во время итерации.
Если пользователь попытается выполнить итерацию после того, как он выдал все возможные числа следует вывести «Out of number!».
_Примечание: вообще не используйте функцию range()_
Пример:
er1 = EvenRange(7,11)
next(er1)
8
next(er1)
10
next(er1)
"Out of numbers!"
next(er1)
"Out of numbers!"
er2 = EvenRange(3, 14)
for number in er2:
    print(number)
4 6 8 10 12 "Out of numbers!"

"""


class EvenRange:
    """
    Класс генератора который выводит только четные числа в заданном диапазоне
    """

    def __init__(self, start: int, stop: int):
        self.start = start + 1 if start % 2 else start
        self.stop = stop

    def __next__(self):
        if self.start < self.stop:
            if self.start % 2 == 0:
                self.start += 2
            else:
                self.start += 1
            result = self.start
            return result
        else:
            print(f"Out of number")
            raise StopIteration

    def __iter__(self):
        return self


er1 = EvenRange(3, 14)
next(er1)
next(er1)
next(er1)
next(er1)
next(er1)
next(er1)
next(er1)
