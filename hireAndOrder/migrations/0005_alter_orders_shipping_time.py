# Generated by Django 4.0.6 on 2022-07-29 05:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hireAndOrder', '0004_remove_orders_cartitems_orders_products_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='shipping_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 29, 13, 40, 41, 208218), editable=False, null=True),
        ),
    ]
