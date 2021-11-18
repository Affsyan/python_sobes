"""
Усовершенствовать родительский класс таким образом,
чтобы получить доступ к защищенным переменным. Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


class ItemDiscount:
    __name = "Диван"
    __price = 15000


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return print(f'{self._ItemDiscount__name} стоимость {self._ItemDiscount__price}')


test = ItemDiscount()
ItemDiscountReport().get_parent_data()