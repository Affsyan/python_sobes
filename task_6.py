"""
Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно.
Внутри каждого поместить функцию get_info, которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены. Далее реализовать выполнение каждой из функции тремя способами.
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReportName(ItemDiscount):
    def get_info(self):
        print(f'Имя товара {self.name}')


class ItemDiscountReportPrice(ItemDiscount):
    def get_info(self):
        print(f'Цена товара {self.price}')


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount):
        ItemDiscount.__init__(self, name, price)
        self.discount = discount

    def get_parent_data(self):
        return print(f'{self.name} стоимость {self.price}')

    def __str__(self):
        return f'{self.name} стоимость с учётом скидки {self.discount}% составляет: ' \
               f'{self.price - self.price / 100 * self.discount}'


print(ItemDiscountReport("Диван", 15000, 10))

name = ItemDiscountReportName("Диван", 15000)
price = ItemDiscountReportPrice("Диван", 15000)

name.get_info()
price.get_info()
