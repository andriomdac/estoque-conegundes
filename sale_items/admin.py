from django.contrib import admin


class SaleItemAdmin(admin.ModelAdmin):
    list_display = ["store_item", "sale", "created_at", "updated_at",]
