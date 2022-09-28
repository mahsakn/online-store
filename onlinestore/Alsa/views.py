from django.shortcuts import render
from django.views.generic import ListView

from Products.models import Product


def test5(request):
    return render(request, "Cart/cart.html", {})


def test6(request):
    return render(request, "Products/product_category_sidebar.html", {})


class Home(ListView):

    def get(self, request):
        newproduct = Product.objects.all().order_by('-date_create')[0:10]
        product = Product.objects.all().order_by('-date_create')[10:20]
        context = {
            'new_products': newproduct,
            'product': product
        }
        return render(request, 'home.html', context)
