# Generated by Django 4.0.6 on 2022-07-20 08:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_options'),
        ('hireAndOrder', '0003_alter_orders_shipping_time_ordertransection_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='cartitems',
        ),
        migrations.AddField(
            model_name='orders',
            name='products',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.products'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='shipping_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 20, 16, 18, 28, 34068), editable=False, null=True),
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]