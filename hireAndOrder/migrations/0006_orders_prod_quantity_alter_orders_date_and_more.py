# Generated by Django 4.0.2 on 2022-07-31 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hireAndOrder', '0005_alter_orders_shipping_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='prod_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 7, 31, 15, 27, 6, 470702)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='shipping_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 31, 17, 27, 6, 470702), editable=False, null=True),
        ),
    ]
