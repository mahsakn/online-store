import imp
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from User.utils import create_otp_code , create_end_time
from User.managers import CustomUserManager
from User.valid import PhoneField

class OTPType(models.IntegerChoices):
    AUTHENTICATE = (1, _("AUTHENTICATE"))
    FORGETPASSWORD = (2, _("FORGETPASSWORD"))


class Address(models.Model):
    add = models.CharField(
        max_length=255,
        verbose_name=("address"),
        help_text=_("Enter your Address")
    )
    
    def __str__(self):
        return self.add


class User(AbstractUser):
    username = None
    email = models.EmailField(
        'email address', 
        unique = True,
        help_text = _("your email")
        )

    phone = PhoneField(
        max_length=16,
        blank=True,
        null=True,
        help_text=_("your phonenumber"),
        verbose_name=_('phonenumber')
        )
      
    profile_image = models.FileField(
        default='/profile_images/user_profile.jpg',
        upload_to='profile_images/',
        null=True,
        blank=True,
        help_text=_("upload your image"),
        verbose_name=_('image')
        )

    address = models.ManyToManyField(
        Address,
        blank = True,
        help_text = _('your address'),
        verbose_name = _('address')

    )

    is_email_verified = models.BooleanField(
        help_text = _("Email validity"),
        default = False
        )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.email

class OTP(models.Model):
    code = models.CharField(
        max_length=11,
        default=create_otp_code,
        verbose_name=_("code"),
        help_text=_("code"),
        unique=True
        )
    exp_time = models.DateTimeField(
        default=create_end_time,
        verbose_name=_("exp_time"),
        help_text=_("Time out")
        )
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="otp_user",
        verbose_name=_("user"),
        help_text=_("user")
        )
    type = models.IntegerField(
        choices=OTPType.choices,
        verbose_name=_("type"),
        help_text=_("type")
        )

    is_used = models.BooleanField(
        default=False ,
        verbose_name=_("is_used"),
        help_text= _("Specifies the code used or not")
    )

    @property
    def is_expired(self):
        if self.exp_time < timezone.now():
            return True
        return False

    def __str__(self):
        return self.code



    

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return self.add
