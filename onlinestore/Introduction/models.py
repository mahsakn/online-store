from django.db import models
from django.utils.translation import gettext as _


class Intro(models.Model):
    address = models.CharField(
        max_length=255,
        verbose_name=_("address"),
        help_text=_("Enter your Address"),
        null=True,
        blank=True
    )
    phone_number = models.PositiveBigIntegerField(
        verbose_name=_("phone_number"),
        help_text=_("Enter your phone number"),
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to="Introduction/Intro",
        help_text=_("Upload your photo"),
        null=True,
        blank=True
    )
    discription = models.TextField(
        verbose_name=_("discretion"),
        help_text=_("Enter your discription"),
        null=True,
        blank=True
        )

    class Meta:
        verbose_name = "Introduction"
        verbose_name_plural = "Introductions"

    def __str__(self) -> str:
        return self.id
