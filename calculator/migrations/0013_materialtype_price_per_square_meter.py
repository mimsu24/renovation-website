# Generated by Django 5.0.4 on 2024-05-06 09:16

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0012_bathroomitem_add'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialtype',
            name='price_per_square_meter',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
    ]
