"""
Проверить механизм наследования в Python.
Для этого создать два класса. Первый — родительский (ItemDiscount), должен содержать статическую информацию о товаре:
название и цену. Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data),
отвечающую за отображение информации о товаре в одной строке.
Проверить работу программы, создав экземпляр (объект) родительского класса.
"""


class ItemDiscount:
    name = "Диван"
    price = 15000


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return print(f'{self.name} стоимость {self.price}')


test = ItemDiscount()
ItemDiscountReport().get_parent_data()
