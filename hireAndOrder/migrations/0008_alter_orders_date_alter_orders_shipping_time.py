# Generated by Django 4.0.6 on 2022-08-04 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hireAndOrder', '0007_alter_orders_date_alter_orders_shipping_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 8, 4, 22, 0, 49, 996412)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='shipping_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 5, 0, 0, 49, 996412), editable=False, null=True),
        ),
    ]
