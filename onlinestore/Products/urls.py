from django.urls import path
from Products.views import *
from . import views

app_name = "Product"
urlpatterns = [
    path('detailproduct/<int:product_id>/', product_detail.as_view(), name="detailproduct"),
    path('listproduct/',product_list.as_view(),name="listproduct"),
    path('view_wishlist/', view_wishlist.as_view(), name="view_wishlist"),
    path('add_wishlist/', add_to_wishlist, name="add_wishlist"),
    path('add_wishlist/<int:product_id>', add_to_wishlist, name="add_wishlist"),
    path('del_wishlist/<int:pk>', delete_wishlist, name="del_wishlist"),
]
