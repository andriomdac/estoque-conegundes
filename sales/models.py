from django.db import models


class Sale(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Venda {self.pk} criada em {self.created_at} - R$ {selftotal_amount}"