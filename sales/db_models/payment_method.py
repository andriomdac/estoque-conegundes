from django.db import models
from sales.models import Sale
from django.core.validators import MinValueValidator


class PaymentMethodChoice(models.Model):
    name = models.CharField(
        max_length=50
        )

    def __str__(self):
        return self.name


class PaymentMethodValue(models.Model):
    method = models.ForeignKey(
        PaymentMethodChoice,
        on_delete=models.PROTECT
        )
    sale = models.ForeignKey(
        to=Sale,
        on_delete=models.CASCADE,
        related_name='payment_methods',
        default=1
        )
    total_amount = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0.00,
        validators=[MinValueValidator(
            0.01,
            message='O valor deve ser maior que zero.'
            )]
        )

    def __str__(self):
        return self.method
