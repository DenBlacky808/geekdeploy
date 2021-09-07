from django.shortcuts import render
from .models import ProductCategory, Product


def main(request):
    content = {'title': 'Магазин'}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    categories = ProductCategory.objects.all()[:4]
    products = Product.objects.all()[:4]
    content = {'title': 'Каталог', 'products': products, 'pk': pk, 'categories': categories}
    return render(request, 'mainapp/products.html', content)


def contact(request):
    content = {'title': 'Контакты'}
    return render(request, 'mainapp/contact.html', content)

