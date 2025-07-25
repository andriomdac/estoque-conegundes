# Generated by Django 5.2 on 2025-05-20 01:13

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethodChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethodValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.01, message='O valor deve ser maior que zero.')])),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payments.paymentmethodchoice')),
                ('sale', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='payment_methods', to='sales.sale')),
            ],
        ),
    ]
