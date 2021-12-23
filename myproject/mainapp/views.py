from django.shortcuts import render
from .models import ProductList, ProductCategory


def category(request):
    title = 'категории'
    category_name = ProductCategory.on_site.all()
    products = ProductList.on_site.prefetch_related('category').all()
    context = {
        'title': title,
        'products': products,
        'category': category_name,
    }
    return render(request=request, template_name='category.html', context=context)


def category_filter(request, pk=0):
    title = 'категории'
    if pk == 0:
        category_name = ProductCategory.on_site.all()
        products = ProductList.on_site.prefetch_related('category').all()
        context = {
            'title': title,
            'products': products,
            'category': category_name,
        }
    else:
        category_name = ProductCategory.on_site.exclude(id=pk).all()
        filter_name = ProductCategory.on_site.filter(id=pk)
        for _ in filter_name:
            products = ProductList.on_site.prefetch_related('category').filter(category=_)
        context = {
            'title': title,
            'products': products,
            'category': category_name,
        }

    return render(request=request, template_name='category.html', context=context)
