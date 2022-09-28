from django.db.models import Q
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from Comment.forms import Comment
from Products.models import Category
from Products.utils import (
    Color_product,
    List_product,
    category,
    comment_product,
    filtering,
    search
)
from Products.models import (
    Product,
    WishList,
)
from User.models import User


class product_detail(DetailView):
    model = Product
    template_name = "Products/product_details.html"
    context_object_name = "singleproduct"
    pk_url_kwarg = "product_id"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        obj_product = self.get_object().return_category
        context["objproduct"] = obj_product

        context["colorproduct"] = Color_product(self.kwargs["product_id"])

        context["listproduct"] = List_product(self.kwargs["product_id"])

        comentform = Comment()

        context["commentform"] = comentform

        context["commentproduct"] = comment_product(self.kwargs["product_id"])

        if not self.request.user.is_anonymous:
            comentform.fields['emaill'].initial = self.request.user.email

        return context


class product_list(ListView):
    model = Product
    template_name = "Products/product_category.html"
    context_object_name = "productlist"
    paginate_by = 12

    def get_queryset(self):
        qs = super().get_queryset()
        return qs


    def get_context_data(self, **kwargs):
        cntx = super().get_context_data(**kwargs)
        cntx["search_get"] = self.request.GET.get("search")
        cntx["cat_get"] = self.request.GET.get("cat")
        if self.request.GET.get('search', ''):
            cntx["productlist"] = search(self.request.GET.get('search',''))
            cntx["type"] = 'نتایج جستجو'
        if self.request.GET.get('cat',''):
            cntx["productlist"] = category(self.request.GET.get('cat',''))
            cat = Category.get_cat(self.request.GET.get('cat',''))
            if cat.category_p:
                cntx["type"] = f"{cat.category_p.title}/{cat.title}"
            else:
                cntx["type"] = f"{cat.title}"
        if self.request.GET.get('ftr',''):
            cntx["productlist"] = filtering(self.request.GET.get('ftr',''))

        
        

        return cntx


class view_wishlist(ListView):
    model = WishList
    template_name = "Products/wishlist.html"
    context_object_name = "wish_list"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["wishlist"] = self.get_queryset()
        return context

    def get_queryset(self):
        wl, created = WishList.objects.get_or_create(user=self.request.user)
        return wl


@login_required(login_url='/user/login')
def add_to_wishlist(request, product_id=None):
    user = get_object_or_404(User, email=request.user.email)
    product = get_object_or_404(Product, Q(id=request.POST.get("id")) | Q(id=product_id))
    wishlist, created = WishList.objects.get_or_create(user=user)
    wishlist.product.add(product)
    wishlist.save()
    return redirect("product:view_wishlist")


@login_required(login_url='/user/login')
def delete_wishlist(request, pk):
    product = Product.objects.get(id=pk)
    wishlist = request.user.wishlisttocustomer.all().first().product.remove(product)
    return redirect("product:view_wishlist")


