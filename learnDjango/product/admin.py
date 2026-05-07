from django.contrib import admin
from .models import Product
# Register your models here.
# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('nama', 'deskrispi','harga', 'is_active', 'stok')

# admin.site.register(Product)