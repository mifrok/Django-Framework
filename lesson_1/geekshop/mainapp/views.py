import random

from django.shortcuts import render
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404
from basketapp.models import Basket

products = Product.objects.all()[:4]
categories = ProductCategory.objects.all()
basket = Basket.objects.all()

links = [{'href': 'index', 'title': 'Магазин', 'menu': 'домой'},
         {'href': 'products:index', 'title': 'Каталог', 'menu': 'продукты'},
         {'href': 'contacts', 'title': 'Контакты', 'menu': 'контакты'}]

content = {
    'titles': links,
    'products': products,
    'categories': categories,
    'basket': basket
}


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category). \
                        exclude(pk=hot_product.pk)[:3]

    return same_products


def main(request):
    return render(request, 'index.html', context=content)


def products(request, pk=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }

        return render(request, 'products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'old_links': links,
        'hot_product': hot_product,
        'basket': basket,

    }
    return render(request, 'products.html', context=content)


def contact(request):
    return render(request, 'contact.html', context=content)


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'product.html', content)

# Create your views here.
