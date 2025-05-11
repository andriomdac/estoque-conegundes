from django.db import models
from django.core.validators import MinValueValidator
from .store_item import StoreItem


class StoreItemPrice(models.Model):
    store_item = models.ForeignKey(StoreItem, on_delete=models.PROTECT, related_name='prices')
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    @property
    def profit(self):
        return self.selling_price - self.cost_price

    def __str__(self):
        return f"{self.store_item.product.name} - {self.selling_price}"
