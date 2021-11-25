from django.db import models


class ProductList (models.Model):
    name = models.CharField(
        verbose_name='Название товара',
        max_length=64,
    )

    price = models.PositiveIntegerField(
        verbose_name='Цена',
        default=0,
    )

    unit = models.CharField(
        verbose_name='Единица измерения',
        max_length=64,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='Колличество',
        default=0,
    )

    supplier_name = models.CharField(
        verbose_name='Имя поставщика',
        max_length=64,
    )

    data = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_created=True,
        auto_now_add=True,
    )

    class Meta:
        verbose_name_plural = "Список товаров"

    def __str__(self):
        return self.name
