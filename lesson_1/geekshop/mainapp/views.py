from django.shortcuts import render

# title = [{'index': 'Магазин'},
#          {'products': 'Каталог'},
#          {'contact': 'Контакты'}]
links = [{'href': 'index', 'title': 'Магазин', 'menu': 'домой'},
        {'href': 'products', 'title': 'Каталог', 'menu': 'продукты'},
        {'href': 'contacts', 'title': 'Контакты', 'menu': 'контакты'}]
content = {
    'titles': links,
}


def main(request):
    return render(request, 'index.html', context=content)


def products(request):
    return render(request, 'products.html', context=content)


def contact(request):
    return render(request, 'contact.html', context=content)

# Create your views here.
