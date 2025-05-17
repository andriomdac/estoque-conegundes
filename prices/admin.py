from django.contrib import admin
from .models import StoreItemPrice

@admin.register(StoreItemPrice)
class StoreItemPriceAdmin(admin.ModelAdmin):
    list_display = ["store_item", "cost_price", "selling_price", "created_at", "updated_at", "active"]