from django.contrib import admin
from stores.models import Store


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at", "active"]