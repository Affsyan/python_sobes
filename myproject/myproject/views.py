from django.shortcuts import render
from mainapp.models import ProductList


def index(request):
    title = 'главная'
    products = ProductList.objects.prefetch_related('category').all()
    context = {
        'title': title,
        'products': products,
    }
    return render(request=request, template_name='index.html', context=context)

