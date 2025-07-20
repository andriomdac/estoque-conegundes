from django.contrib import admin
from .models import Brand


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