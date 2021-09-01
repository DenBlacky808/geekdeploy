from django.shortcuts import render


def main(request):
    name = {'title': 'Магазин'}
    return render(request, 'mainapp/index.html', name)


def products(request):
    name = {'title': 'Каталог'}
    return render(request, 'mainapp/products.html', name)


def contact(request):
    name = {'title': 'Контакты'}
    return render(request, 'mainapp/contact.html', name)


