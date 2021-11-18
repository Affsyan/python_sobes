"""
Реализовать расчет цены товара со скидкой.
Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса
(метод init, в который должна передаваться переменная — скидка), и перегрузку метода str дочернего класса.
В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса).
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount):
        ItemDiscount.__init__(self, name, price)
        self.discount = discount

    def get_parent_data(self):
        return print(f'{self.name} стоимость {self.price}')

    def __str__(self):
        return f'{self.name} стоимость с учётом скидки {self.discount} составляет:' \
               f'{self.price - self.price/100 * self.discount}'


print(ItemDiscountReport("Диван", 15000, 10))
