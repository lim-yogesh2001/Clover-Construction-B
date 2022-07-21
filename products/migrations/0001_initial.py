# Generated by Django 4.0.2 on 2022-07-15 18:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stores', '0005_alter_categories_store_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('prod_image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.categories')),
                ('store_id', models.ManyToManyField(to='stores.Store')),
            ],
        ),
    ]