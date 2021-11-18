"""
Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
"""


class ItemDiscount:
    __name = "Диван"
    __price = 15000


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return print(f'{self.name} стоимость {self.price}')


test = ItemDiscount()
ItemDiscountReport().get_parent_data()
