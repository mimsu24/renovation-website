# Generated by Django 5.0.4 on 2024-04-15 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_alter_housetype_add'),
    ]

    operations = [
        migrations.RenameField(
            model_name='housetype',
            old_name='typeofhouse',
            new_name='typesofhouse',
        ),
    ]