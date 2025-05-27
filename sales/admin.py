from django.contrib import admin


class SaleAdmin(admin.ModelAdmin):
    list_display = ["total_amount", "created_at", "updated_at",]
