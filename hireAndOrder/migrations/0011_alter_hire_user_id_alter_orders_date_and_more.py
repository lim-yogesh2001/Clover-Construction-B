# Generated by Django 4.0.6 on 2022-08-06 23:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hireAndOrder', '0010_alter_orders_date_alter_orders_shipping_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hire',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 7, 5, 21, 12, 132685)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='shipping_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 7, 7, 21, 12, 132685), editable=False, null=True),
        ),
    ]
