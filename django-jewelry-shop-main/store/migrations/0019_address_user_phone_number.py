# Generated by Django 5.1.6 on 2025-03-28 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='user_phone_number',
            field=models.IntegerField(default=0),
        ),
    ]
