from django.contrib import admin

from .models import (
    Category,
    Details,
    Product,
    Property,
    WishList,
    Color
)


admin.site.register(Category)
admin.site.register(Product)

admin.site.register(WishList)
admin.site.register(Color)


class CartItemInline(admin.StackedInline):
    model = Details


@admin.register(Property)
class CartModelAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
