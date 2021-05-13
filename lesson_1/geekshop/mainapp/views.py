from django.shortcuts import render
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404
from basketapp.models import Basket

products = Product.objects.all()[:4]
categories = ProductCategory.objects.all()

links = [{'href': 'index', 'title': 'Магазин', 'menu': 'домой'},
         {'href': 'products:index', 'title': 'Каталог', 'menu': 'продукты'},
         {'href': 'contacts', 'title': 'Контакты', 'menu': 'контакты'}]

content = {
    'titles': links,
    'products': products,
    'categories': categories,
}


def main(request):
    return render(request, 'index.html', context=content)


def products(request, pk=None):
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = []
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

    same_products = Product.objects.all()[3:5]

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'old_links': links,
    }
    return render(request, 'products.html', context=content)


def contact(request):
    return render(request, 'contact.html', context=content)

# Create your views here.
