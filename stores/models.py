from django.db import models
from django.core.validators import MinValueValidator
from products.models import Product


class Store(models.Model):
    name = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class StoreCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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
