# Generated by Django 5.1.6 on 2025-02-21 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_remove_cart_shiping_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_charge',
            field=models.DecimalField(decimal_places=2, default=99.0, max_digits=10),
        ),
    ]
