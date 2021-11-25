from django.shortcuts import render

from e_commerce.stores.models import Category, Product


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    products = Product.objects.all()
    return render(request, 'stores/home.html', {'products': products})
