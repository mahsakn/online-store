from django.db import models
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext as _

from User.models import User


class Category(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        help_text=_("Please select your product name."),
        verbose_name=_('title')
    )
    category_p = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='catproductmodel',
        verbose_name=_('title'),
        help_text=_("Please select the desired product type"),
        null=True,
        blank=True
    )

    @classmethod
    def get_cat(cls, id):
        cat = get_object_or_404(Category, pk=id)
        return cat

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.title


class Color(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        help_text=_("Choose the color of your product"),
        verbose_name=_('color'),
        null=True
    )

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text=_("Please select your product name."),
        verbose_name=_('product name')
    )
    image = models.ImageField(
        upload_to="Products",
        null=True, blank=True,
        help_text=_("upload your image"),
        verbose_name=_('image')
    )
    image1 = models.ImageField(
        upload_to="Products",
        null=True,
        blank=True,
        help_text=_("upload your image"),
        verbose_name=_('image')
    )
    image2 = models.ImageField(
        upload_to="Products",
        null=True, blank=True,
        help_text=_("upload your image"),
        verbose_name=_('image')
    )
    price = models.PositiveIntegerField(
        verbose_name=_('price'),
        help_text=_("Enter the product price")
    )
    capacity = models.PositiveIntegerField(
        verbose_name=_('capacity'),
        help_text=_("product inventory")
    )
    discription = models.TextField(
        verbose_name=_('discription'),
        help_text=_("Relevant descriptions"),
        null=True,
        blank=True
    )
    color = models.ManyToManyField(
        Color,
        blank=True,
        help_text=_("Choose the color of your product"),
    )
    brand = models.CharField(
        max_length=16,
        null=True,
        help_text=_("Enter your product brand"),
    )
    cat = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        related_name="producttocat",
        help_text=_("category")
    )
    date_create = models.DateTimeField(
        auto_now_add=True,
        help_text=_("date")
    )
    data_update = models.DateTimeField(
        auto_now=True,
        help_text=_("date update")
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return self.name

    @property
    def return_category(self):
        category = Category.objects.get(pk=self.cat.id)
        return category

    def get_absolute_url(self):
        return reverse('Product:product_detail', args=[self.id])


class WishList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="wishlisttocustomer",
        help_text=_("user"),
        null=True,
        blank=True
    )
    product = models.ManyToManyField(
        Product,
        help_text=_("product")
    )
    datetime = models.DateTimeField(
        auto_now=True,
        verbose_name=_('date and time'),
        help_text=_("data and time")
    )

    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"

    def __str__(self) -> str:
        return self.user.email


class Property(models.Model):
    property_name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text=_("property name")
    )
    cat_id = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='propertytocat',
        help_text=_("category")
    )

    def __str__(self) -> str:
        return self.property_name


class Details(models.Model):
    pro_id = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='detailstoproperty',
        help_text=_("property"),
        null=True
    )
    product_id = models.ManyToManyField(Product)
    detail = models.CharField(
        max_length=400,
        help_text=_("product"),
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return self.detail
