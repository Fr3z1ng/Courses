"""
2. Создать 2 класса Truck и Sedan, которые являются наследниками Auto.
Класс Truck имеет дополнительный обязательный атрибут max_load.
Переопределить метод drive, который перед появление сообщения
«Car <brand> <mark> drives» выводит сообщение «Attention!».
Реализовать дополнительный метод load.
его вызове происходит пауза в 1 секунду (используя модуль time),
затем выводится сообщение «load», а затем снова происходит пауза в 1 секунду.
Класс Sedan имеет дополнительный метод обязательный атрибут max_speed и при вызове метода drive,
после появления сообщения «Car <brand> <mark> drives»,
выводит сообщение «max speed of sedan <brand> <mark> is <max_speed>».
Инициализировать по 2 отдельных объекта этих классов, проверить работы их методов и атрибутов
(вызвать методы, атрибуты вывести в печать)
"""
from time import sleep


class Auto():
    """
    Класс выводит сообщения машина едет или остановилась,так же добавляет плюс 1 год
    с помощью метода use
    """
    color = "black"
    weight = 2000

    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def drive(self):
        print(f"Car {self.brand} {self.mark} drives")

    def stop(self):
        print(f"Car {self.brand} {self.mark} stops")

    def use(self):
        self.age += 1


class Truck(Auto):
    """
    Дочерний класс Auto, перугружен метод drive и добавлен метод load
    """
    def __init__(self, brand, age, mark, max_load):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def drive(self):
        print("Attention!")
        print(f"Car {self.brand} {self.mark} drives")

    def load(self):
        sleep(1)
        print("load")
        sleep(1)


class Sedan(Auto):
    """
    Дочерний класс Auto,перегружен метод drive
    """
    def __init__(self, brand, age, mark, max_speed):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def drive(self):
        print(f"Car {self.brand} {self.mark} drives")
        print(f"max speed of sedan {self.brand} {self.mark} is {self.max_speed}")


sedan = Sedan("Sedan", 1997, "Something", 250)
truck = Truck("Truck", 1986, "B5", 7000)
truck.drive()
truck.load()
truck.stop()
sedan.drive()
sedan.use()
print(sedan.age)
print(truck.max_load)
print(sedan.max_speed)