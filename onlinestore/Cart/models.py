from django.db import models
from django.utils.translation import gettext as _

from User.models import User
from Products.models import Product


class CartMe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='CartmetoCustomer',
        null=True,
        blank=True,
        help_text=_("user name")
    )
    product = models.ManyToManyField(
        Product,
        through="CartItem",
        help_text=_("products")
    )
    priceTotal = models.PositiveIntegerField(
        verbose_name=_("priceTotal"),
        null=True,
        blank=True,
        help_text=_("price total")
    )
    discount = models.CharField(
        max_length=10,
        verbose_name=_("discount"),
        help_text=_("discount")
    )
    date = models.DateTimeField(
        auto_now=True,
        help_text=_("date")
        )
    ispaid = models.BooleanField(
        default=False,
        help_text=_("ispaid")
        )
    factor = models.JSONField(
        null=True,
        blank=True,
        verbose_name=_("factor"),
        help_text=_("Purchase Invoice")
    )

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Carts"

    def __str__(self) -> str:
        return self.user.email


class CartItem(models.Model):
    cart = models.ForeignKey(
        CartMe,
        on_delete=models.CASCADE,
        related_name='CartItemtoCartMe',
        null=True,
        help_text=_("cart")
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='CartItemtoProduct',
        null=True,
        help_text=_("products")
    )
    salesman = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        help_text=_("salesman")
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class History(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='HistorytoCustomer',
        null=True,
        blank=True,
        help_text=_("Customer")
    )
    cartme = models.ManyToManyField(
        CartMe,
        help_text=_("products")
    )
    date = models.DateTimeField(
        auto_now_add=True,
        help_text=_("date")
    )
    date_update = models.DateTimeField(
        auto_now=True,
        help_text=_("date update")
        )

    class Meta:
        verbose_name = "History"
        verbose_name_plural = "Historys"

    def __str__(self) -> str:
        return self.customer.email
