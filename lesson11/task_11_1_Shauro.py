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
    cost: float
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
        self.summa_order = 0
        self.money_order = 0
        self.weight_order = 0
        self.cost_order = 0
        self.count_order = 0
        self.some_list_order = []

    def properties(self, *args):
        """
        Метод подсчитывает общую сумму,количество и вес заказа
        """
        self.some_list_order += list(args)
        for i in args:
            self.count_order += i.count
            self.cost_order += i.cost
            self.weight_order += i.weight
        return self.count_order, self.cost_order, self.weight_order

    def pay_money(self, money_order: int):
        """
        Подсчитывает сколько необходимо заплатить за заказ или выдать сдачи клиенту
        """
        self.money_order += money_order
        self.summa_order = self.cost_order - self.money_order
        if self.summa_order > 0:
            print(f"Вам нужно доплатить {self.summa_order} р")
        else:
            print(f"Ваша овсянка,Сэр! {abs(self.summa_order)} р сдачи")


order_1 = Order()
order_1.properties(dish_1, dish_2)
print(order_1.count_order)
print(order_1.cost_order)
print(order_1.weight_order)
order_1.pay_money(25)
order_1.pay_money(40)
