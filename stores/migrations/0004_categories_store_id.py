# Generated by Django 4.0.6 on 2022-07-13 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='store_id',
            field=models.ManyToManyField(to='stores.store'),
        ),
    ]