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


def search(srch):
    data = Product.objects.filter(name__contains=srch).order_by('-id')
    return data

def category(c):
    data = Product.objects.filter(cat__id=c).order_by('-id')
    return data

def filtering(ftr):
    for key,value in ftr.items():
        if key == "price":
            if value!= "": 
                price=value.split(",")
                filtered_product = filtered_product.filter(price__range=(int(price[0]),int(price[1])))
            else : continue
        elif key == "brand":
            if value!= "":
                filtered_product = filtered_product.filter(brand = value)
            else : continue
            
            
    return filtered_product
