from django.contrib import admin
from stores.models import Store, StoreCategory, StoreItem, StoreItemPrice

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at", "active"]

@admin.register(StoreCategory)
class StoreCategoryAdmin(admin.ModelAdmin):
    list_display = ["pk","name",]

@admin.register(StoreItem)
class StoreItemAdmin(admin.ModelAdmin):
    list_display = ["store", "product", "category", "quantity", "created_at", "updated_at", "active",]

@admin.register(StoreItemPrice)
class StoreItemPriceAdmin(admin.ModelAdmin):
    list_display = ["store_item", "cost_price", "selling_price", "created_at", "updated_at", "active"]