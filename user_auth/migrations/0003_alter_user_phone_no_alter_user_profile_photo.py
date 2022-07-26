# Generated by Django 4.0.6 on 2022-07-12 06:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_alter_user_address_alter_user_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Please Enter the number that starts with 9 and has 10 digits.', regex='^\\??\\d{9,11}$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
