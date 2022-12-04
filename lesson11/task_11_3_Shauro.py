"""
3. Реализуйте класс DataObject который имеет обязательный атрибут data (произвольного типа данных)
Реализуйте класс очередь (Deque) с атрибутом класса deque в котором будут хранится элементы добавляемые в очередь,
Класс Deque имеет методы
- append_left для добавления элемента в начало очереди deque
- append_right для добавления элемента в конец очереди deque
(в данных методах необходимо реализовать возможность добавления в очередь только экземпляров класса DataObject (и его дочерних),
а также проверку длины очереди — одновременно там может находится не более 5 элементов — в случае добавления 6 элемента добавление не производится и
пользователю выдается сообщение о переполнении очереди).
- pop_left — удаляет из очереди первый элемент слева и возвращает его
- pop_right - удаляет из очереди первый элемент справа и возвращает его
При реализации методов класса Deque воспользуйтесь методами класса (classmethod)
"""
from typing import Any
from dataclasses import dataclass


@dataclass
class DataObject:
    """
    Класс для передачи любого типа данных
    """
    data: Any


data_1 = DataObject(15)
data_2 = DataObject(20)


class Deque:
    """
    Класс хранит данные в очереди
    """
    deque = []

    @classmethod
    def append_left(cls, other: Any):
        """
        Метод добавляет элемент в очередь слева и проверяет является ли он объектом класса DataObject(или его дочерним)
        """
        if len(cls.deque) < 5:
            if isinstance(other, DataObject):
                cls.deque.insert(0, other.data)
                return cls.deque
        else:
            print("Очередь переполнена,удалите один элемент")
            return cls.deque

    @classmethod
    def append_right(cls, other: Any):
        """
        Метод добавляет элемент в очередь справа и проверяет является ли он объектом класса DataObject(или его дочерним)
        """
        if len(cls.deque) < 5:
            if isinstance(other, DataObject):
                cls.deque.append(other.data)
                return cls.deque
        else:
            print("Очередь переполнена,удалите один элемент")
            return cls.deque

    @classmethod
    def pop_left(cls):
        """
        Метод удаляет элементы из очереди слева и возвращает его
        """
        return cls.deque.pop(0), cls.deque

    @classmethod
    def pop_right(cls):
        """
        Метод удаляет элементы из очереди справа и возвращает его
        """
        return cls.deque.pop(-1), cls.deque


print(Deque.append_left(data_1))
print(Deque.append_left(data_2))
print(Deque.append_right(data_1))
print(Deque.append_right(data_1))
print(Deque.append_left(data_1))
print(Deque.pop_left())
print(Deque.pop_right())
