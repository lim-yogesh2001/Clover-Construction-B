from django.contrib import admin
from .models import Department, Worker

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    empty_value_display = '--empty--'
    list_display = ('id', 'title', 'image',)

class WorkerAdmin(admin.ModelAdmin):
    empty_value_display = '--empty--'
    list_filter = ('departments',)
    list_per_page = 5
    list_display = ('id', 'name', 'address', 'DOB', 'email', 'experience', 'departments', 'isFavorite', 'contact_no',)

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Worker, WorkerAdmin)