# Generated by Django 5.1.6 on 2025-04-07 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_order_current_latitude_order_current_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='current_latitude',
        ),
        migrations.RemoveField(
            model_name='order',
            name='current_longitude',
        ),
    ]
