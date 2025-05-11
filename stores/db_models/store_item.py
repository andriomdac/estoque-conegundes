from django.db import models
from django.core.validators import MinValueValidator
from products.models import Product
from .store import Store
from .category import StoreCategory


class StoreItem(models.Model):
    store = models.ForeignKey(Store, on_delete=models.PROTECT, related_name='store_items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='store_items')
    category = models.ForeignKey(StoreCategory, on_delete=models.PROTECT, related_name='store_items')
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def latest_active_price(self):
        return self.prices.filter(active=True).order_by('-created_at').first()

    def __str__(self):
        return f"{self.product.name} - {self.store.name}"
