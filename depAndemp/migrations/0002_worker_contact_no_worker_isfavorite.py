# Generated by Django 4.0.6 on 2022-08-04 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depAndemp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='contact_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='worker',
            name='isFavorite',
            field=models.BooleanField(default=False),
        ),
    ]
