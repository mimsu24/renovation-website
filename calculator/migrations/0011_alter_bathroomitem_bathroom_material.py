# Generated by Django 5.0.4 on 2024-04-26 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0010_rename_items_name_bathroomitem_bathroom_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bathroomitem',
            name='bathroom_material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.materialtype'),
        ),
    ]
