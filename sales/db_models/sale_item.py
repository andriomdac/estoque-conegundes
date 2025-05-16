from django.db import models
from stores.models import StoreItem
from sales.models import Sale

class SaleItem(models.Model):
    store_item = models.ForeignKey(StoreItem, on_delete=models.PROTECT, related_name='sale_item')
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='sale_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.store_item} - {self.sale}"