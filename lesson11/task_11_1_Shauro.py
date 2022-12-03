"""
1. Реализуйте класс Блюдо, описывающее количество, название, стоимость и массу блюда.
Далее создайте несколько инстансов этого класса с описанием блюд.
Реализуйте класс Заказ, в инстанс которого можно было бы добавлять блюда.
Заказ должен содержать вычисляемые свойства: количество, стоимость, масса блюд в заказе.
Также реализуйте дополнительный метод "оплатить" (внесение определенной суммы в счет оплаты заказа)
и дополнительное свойство, обозначающее сумму, которую осталось оплатить (с учетом стоимости заказа и
внесенных с помощью метода «оплатить» денег)
"""
from dataclasses import dataclass


@dataclass
class Dish:
    """
    С помощью датакласса определил класс Блюдо и добавил в него аргументы
    """
    count: int
    name: str
    cost: int
    weight: int


dish_1 = Dish(30, "Цезарь", 15, 500)
dish_2 = Dish(20, "Отбивная", 20, 250)
dish_3 = Dish(10, "Картоха", 5, 1000)


class Order:
    """
    Этот класс принимает инстансы класса Dish, считает общую сумму,количество и вес всего заказа
    так же показывает сколько осталось доплатить или сколько вам дадут сдачи
    """

    def __init__(self):
        self.summa = 0
        self.money = 0
        self.weight = 0
        self.cost = 0
        self.count = 0
        self.list_1 = []

    def properties(self, *args):
        """
        Метод подсчитывает общую сумму,количество и вес заказа
        """
        self.list_1 = [args]
        for value in self.list_1:
            for i in value:
                self.count += i.count
                self.cost += i.cost
                self.weight += i.weight
        return self.count, self.cost, self.weight

    def pay_money(self, money: int):
        """
        Подсчитывает сколько необходимо заплатить за заказ или выдать сдачи клиенту
        """
        self.money = money
        self.summa = self.cost - self.money
        if self.summa > 0:
            print(f"Вам нужно доплатить {self.summa} р")
        else:
            print(f"Ваша овсянка,Сэр! {abs(self.summa)} р")


order_1 = Order()
order_1.properties(dish_1, dish_2)
print(order_1.count)
print(order_1.cost)
print(order_1.weight)
order_1.pay_money(25)
order_1.pay_money(40)
