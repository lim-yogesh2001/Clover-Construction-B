from django.contrib import admin
from .models import Store, Categories
# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'cover_image', 'title', 'address', 'contact_no','is_recent',)
    list_per_page = 5

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_image', 'category_name',)
    list_per_page = 5

admin.site.register(Store, StoreAdmin)
admin.site.register(Categories, CategoryAdmin)