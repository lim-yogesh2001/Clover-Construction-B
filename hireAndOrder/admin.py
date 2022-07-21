from django.contrib import admin
from .models import Orders, Hire, OrderTransection

# Register your models here.
admin.site.register(Orders)
admin.site.register(Hire)
admin.site.register(OrderTransection)