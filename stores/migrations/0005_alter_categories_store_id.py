# Generated by Django 4.0.2 on 2022-07-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_categories_store_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='store_id',
            field=models.ManyToManyField(to='stores.Store'),
        ),
    ]
