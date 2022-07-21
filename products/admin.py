from django.contrib import admin
from .models import Products

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category_id',)
    list_display = ('id', 'title', 'prod_image', 'brand', 'price', 'category_id',)

admin.site.register(Products, ProductAdmin)