from django.shortcuts import render
from .models import ProductCategory, Product

products = Product.objects.all()[:4]
categories = ProductCategory.objects.all()

links = [{'href': 'index', 'title': 'Магазин', 'menu': 'домой'},
        {'href': 'products', 'title': 'Каталог', 'menu': 'продукты'},
        {'href': 'contacts', 'title': 'Контакты', 'menu': 'контакты'}]

content = {
    'titles': links,
    'products': products,
    'categories': categories,
}


def main(request):
    return render(request, 'index.html', context=content)


def products(request):
    return render(request, 'products.html', context=content)


def contact(request):
    return render(request, 'contact.html', context=content)

# Create your views here.
