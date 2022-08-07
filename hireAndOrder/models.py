from django.db import models
from products.models import Products
from django.contrib.auth import get_user_model
from datetime import timedelta, datetime
from depAndemp.models import Worker
    

class Orders(models.Model):
    ship_time = datetime.now() + timedelta(hours=2)
    date = models.DateTimeField(default=datetime.now())
    total = models.IntegerField(default=0)
    status = models.BooleanField(default= False)
    prod_quantity = models.IntegerField(default=0, null=True, blank=True)
    products = models.ForeignKey(Products, on_delete = models.CASCADE)
    user = models.ForeignKey(get_user_model(), null=True, on_delete = models.CASCADE)
    shipping_time = models.DateTimeField(default=ship_time, editable=False, null=True)


    def __str__(self):
        return f"{self.id}"
    
    class Meta:
        verbose_name_plural = "Orders"


class Hire(models.Model):
    worker = models.ForeignKey(Worker, on_delete = models.CASCADE)
    date_of_hire = models.DateTimeField(auto_now=datetime.now())
    user_id = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, null=True)

    def __str__(self):
        return f"{self.worker.name}"


class OrderTransection(models.Model):
    order_id = models.ForeignKey(Orders(), on_delete = models.CASCADE)
    transection_code = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id}"
    
class HireTransection(models.Model):
    hire_id = models.ForeignKey(Hire, on_delete = models.CASCADE)
    transection_code = models.CharField(max_length=400)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Hire {self.id}"
