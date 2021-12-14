from django.db import models
from django.contrib.sites.models import Site


class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name='Категория товара',
        max_length=64,
    )

    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Сайты',
    )

    class Meta:
        verbose_name_plural = "Категория товара"

    def __str__(self):
        return self.name


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

    category = models.ManyToManyField(
        ProductCategory,
        verbose_name='Категория товара',
    )

    site = models.ManyToManyField(
        Site,
        verbose_name='Сайты',
    )

    class Meta:
        verbose_name_plural = "Список товаров"

    def __str__(self):
        return self.name


