from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    A view that shows all products, including sorting and seaching queries
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)
