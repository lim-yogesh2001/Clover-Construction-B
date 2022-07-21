from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.core.validators import RegexValidator


# Create your models here.
class User(AbstractUser):
    first_name = None
    last_name = None
    phone_regex = RegexValidator(regex='^\??\d{9,11}$', message='Please Enter the number that starts with 9 and has 10 digits.')

    full_name = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_no = models.CharField(max_length=10, blank=True, validators=[phone_regex])

    address = models.CharField(max_length=80, blank=True)
    profile_photo = models.ImageField(blank=True, upload_to = 'images/')

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'{self.username}'
    
