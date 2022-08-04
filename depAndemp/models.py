from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Department(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.title}"
    
class Worker(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to= 'images/')
    address = models.CharField(max_length=100)
    DOB = models.DateField(blank=False)
    email = models.EmailField(blank=False)
    qualification = models.TextField()
    experience = models.IntegerField(validators=[MinValueValidator(0)])
    isFavorite = models.BooleanField(default=False)
    contact_no = models.CharField(blank=True, null=True, max_length=10)
    departments = models.ForeignKey(Department, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.name}"
    

