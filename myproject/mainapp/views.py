from django.shortcuts import render
from .models import ProductList, ProductCategory


def category(request):
    title = 'категории'
    category_name = ProductCategory.objects.all()
    products = ProductList.objects.prefetch_related('category').all()
    context = {
        'title': title,
        'products': products,
        'category': category_name,
    }
    return render(request=request, template_name='category.html', context=context)


def category_filter(request, pk):
    title = 'категории'
    category_name = ProductCategory.objects.all()
    products = ProductList.objects.prefetch_related('category').filter(name=category_name).all()
    context = {
        'title': title,
        'products': products,
        'category': category_name,
    }
    return render(request=request, template_name='category.html', context=context)
