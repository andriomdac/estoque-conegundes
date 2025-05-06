from django.contrib import admin
from .models import Product, Brand

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
        "barcode",
        ]
    list_display = [
        "name",
        "brand",
        "barcode",
        ]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    search_fields = [
        "id"
        "name",
        ]
    list_display = [
        "id",
        "name",
        ]