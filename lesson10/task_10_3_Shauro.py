"""
3. Реализуйте класс Counter, который дополнительно принимает начальное значение и конечное значение счетчика.
Если начальное значение не указано, счетчик должен начинаться с 0. Если стоп-значение не указано,
оно должно считаться вверх бесконечно. Если счетчик достигает стоп-значения,
выведите «Maximal value is reached».
Реализовать методы: "increment" (увеличивает счетчик на 1) и "get" (выводит информацию о значении счетчика)
"""


class Counter():
    """
    Методы класса увеличививают счетчик на 1 и выводит информацию о нем
    """

    def __init__(self, start=0, stop=None):
        self.count = start
        self.stop = stop

    def increment(self):
        self.count += 1
        if self.count == self.stop:
            return print("Maximal value is reached")

    def get(self):
        print(self.count)


c = Counter(start=42, stop=43)
c.increment()
c.get()
c_1 = Counter()
c_1.increment()
c_1.get()
c_1.increment()
c_1.get()
