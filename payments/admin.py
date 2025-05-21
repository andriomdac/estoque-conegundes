from django.contrib import admin
from .models import PaymentMethodChoice, PaymentMethodValue

@admin.register(PaymentMethodChoice)
class PaymentMethodChoice(admin.ModelAdmin):
    list_display = [
       "id",
        "name"
    ]