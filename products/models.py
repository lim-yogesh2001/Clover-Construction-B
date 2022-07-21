from django.db import models
from stores.models import Store, Categories
from django.core.validators import MinValueValidator

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=100)
    prod_image = models.ImageField(upload_to='images/')
    description = models.TextField()
    brand = models.CharField(max_length=50)
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    store_id = models.ManyToManyField(Store)
    category_id = models.ForeignKey(Categories, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name_plural = 'Products'