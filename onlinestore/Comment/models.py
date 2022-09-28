from django.db import models
from django.utils.translation import gettext as _

from User.models import User
from Products.models import Product


class rate(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="ratetocustomer",
        verbose_name=_("user"),
        help_text=_("user"),
        null=True,
        blank=True
    )
    product = models.ManyToManyField(Product)
    RATE_CHOICES = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5")
    ]
    rate = models.CharField(
        max_length=1,
        choices=RATE_CHOICES,
        verbose_name=_("rate"),
        help_text=_("Enter your score"),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "rate"
        verbose_name_plural = "rates"

    def __str__(self) -> str:
        return self.user.email


class CommentMe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commenttouser",
        verbose_name=_("user"),
        help_text=_("user"),
        null=True,
        blank=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="commenttoproduct",
        verbose_name=_("product"),
        help_text=_("product"),
        null=True
    )
    comment = models.CharField(
        max_length=255,
        verbose_name=_("comment"),
        help_text=_("Enter your comment"),
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self) -> str:
        return self.user.email
