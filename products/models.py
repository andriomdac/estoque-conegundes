from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=100)
    barcode = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.barcode}"