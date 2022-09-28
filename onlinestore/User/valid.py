
from django.db.models import CharField
from django.core.validators import RegexValidator

class PhoneField(CharField):
    # TODO: add validations on phone numbers : Done xD 
    # TODO: change how field is saved : Done xD

    def _init_(self, max_length=16, *args, **kwargs):
        phone_regex = RegexValidator(regex=r'^(\+98)?9\d{9}$', message="Phone number must be entered in the format: '+98****'. Up to 11 digits allowed.")
        kwargs["validators"] = [phone_regex]
        super()._init_(*args, max_length=max_length, **kwargs)