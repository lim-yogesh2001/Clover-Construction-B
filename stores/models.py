from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Store(models.Model):
    phone_regex = RegexValidator(regex='^\??\d{9,11}$', message='Please Enter the number that starts with 9 and has 10 digits.')

    cover_image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10, validators=[phone_regex])
    store_description = models.TextField()
    is_recent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"

class Categories(models.Model):
    category_image = models.ImageField(upload_to='images/')
    category_name = models.CharField(max_length=50)
    store_id = models.ManyToManyField(Store)

    def __str__(self):
        return self.category_name
    

    class Meta:
        verbose_name_plural = 'Categories'