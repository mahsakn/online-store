from itertools import product
from .models import Category, Product
from django.shortcuts import get_object_or_404


def Color_product(product_id):
    obj_product = get_object_or_404(Product, id=product_id)
    color_product = obj_product.color.all()
    return color_product


def List_product(product_id):
    obj_product = get_object_or_404(Product, id=product_id)
    cat_obj_product = obj_product.return_category

    product_list = Product.objects.filter(cat=cat_obj_product).exclude(id=product_id)

    return product_list


def comment_product(product_id):
    obj_product = get_object_or_404(Product, id=product_id)
    product_comment = obj_product.commenttoproduct.all()

    return product_comment


def search(qs , srch):
    data = qs.filter(name__contains=srch).order_by('-id')
    return data

def category(qs , c):
    data = qs.filter(cat__id=c).order_by('-id')
    return data

def filtering_brand(qs,brn):
    data = qs.filter( brand = brn ).order_by('-id')
    return data

def filtering_price(qs,prc):

    if prc!= "": 
        price=prc.split(",")
        data = qs.filter( price__range = (int(price[0]),int(price[1]))).order_by('-id')
    return data



def filtering(qs , filter):

    if filter.get("cat",""):
        qs = category(qs , filter["cat"])
    if filter.get("search" , "") :
        qs = search(qs , filter["search"] )

    if filter.get("brand" , "") and filter.get("price" , "") :
        price=filter["price"].split(",")
        qs = qs.filter( brand = filter["brand"] , price__range = (int(price[0]),int(price[1])) ).order_by('-id')

    else :
        if filter.get("brand",""):
            qs = filtering_brand(qs,filter["brand"])
        elif filter.get("price",""):
            qs = filtering_price(qs,filter["price"])
        
    return qs