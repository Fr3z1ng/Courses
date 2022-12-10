"""
2. Реализуйте свой пользовательский класс итератора с именем MySquareIterator,
который дает квадраты элементов коллекции, по которой он итерируется.
Пример:
lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)
for el in itr:
	 print(el)
1 4 9 16 25

"""


class MySquareIterator:
    """
    Класс генератора,который будет выводить квадрат чисел в переданном списке
    """
    def __init__(self, lst:list):
        self.lst = lst
        self.start = 0

    def __next__(self):
        try:
            result = self.lst[self.start]
            self.start += 1
        except IndexError:
            raise StopIteration
        return result ** 2

    def __iter__(self):
        return self


lst = [2, 2, 3, 4, 5]
itr = MySquareIterator(lst)
for el in itr:
    print(el)
