from django.contrib import admin
from .models import Sale


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ["total_amount", "created_at", "updated_at",]
