# Generated by Django 4.0.6 on 2022-08-06 03:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hireAndOrder', '0008_alter_orders_date_alter_orders_shipping_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 8, 6, 9, 28, 18, 581287)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='prod_quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='shipping_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 6, 11, 28, 18, 581287), editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
