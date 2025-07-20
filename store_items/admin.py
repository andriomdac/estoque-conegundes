from django.contrib import admin
from .models import StoreItem


@admin.register(StoreItem)
class StoreItemAdmin(admin.ModelAdmin):
    list_display = ["store", "product", "category", "quantity", "created_at", "updated_at", "active",]