# Generated by Django 5.1.6 on 2025-04-08 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_address_latitude_address_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
    ]
