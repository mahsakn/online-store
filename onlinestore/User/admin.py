from django.contrib import admin

from .models import OTP, OTPType, User, Address


admin.site.register(User)
admin.site.register(OTP)

admin.site.register(Address)


