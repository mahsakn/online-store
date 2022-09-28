from django.db import models
from django.utils.translation import gettext_lazy as _

from User.models import User
from Products.models import Product


class notif_user(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notiftocustomer",
        help_text=_("user"),
        null=True,
        blank=True
    )
    product = models.ManyToManyField(
        Product,
        help_text=_("product")
        )
    image_notif = models.ImageField(
        upload_to="Notification/notif_user",
        help_text=_("upload your image"),
        verbose_name=_('image'),
        null=True,
        blank=True
    )
    file_notif = models.FileField(
        upload_to="Notification/notif_user",
        help_text=_("upload your file"),
        verbose_name=_('file'),
        null=True,
        blank=True
    )
    text_notif = models.TextField(
        verbose_name=_('Text'),
        help_text=_("Relevant descriptions"),
    )

    class Meta:
        verbose_name = "notif_user"
        verbose_name_plural = "notif_users"

    def __str__(self) -> str:
        return self.user.email


class News(models.Model):
    image_news = models.ImageField(
        upload_to="Notification/News",
        help_text=_("upload your image"),
        verbose_name=_('image'),
        null=True,
        blank=True
    )
    file_news = models.FileField(
        upload_to="Notification/News",
        help_text=_("upload your file"),
        verbose_name=_('file'),
        null=True,
        blank=True
    )
    text_new = models.TextField(
        verbose_name=_('Text'),
        help_text=_("Relevant descriptions"),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name="newstocustumer",
        help_text=_("user"),
        null=True,
        blank=True
    )
    product = models.ManyToManyField(
        Product,
        help_text=_("product")
        )

    class Meta:
        verbose_name = "News"

    def __str__(self) -> str:
        return self.id
