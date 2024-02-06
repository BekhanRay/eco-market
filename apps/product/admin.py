from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Cart)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "amount", "type_id")
    search_fields = ["name", "type_id", "description"]
    list_filter = ["type_id", "amount", "price"]

    inlines = [ProductImageInline]