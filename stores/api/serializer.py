from rest_framework import serializers
from ..models import Store,Categories

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'cover_image', 'title', 'address', 'contact_no', 'store_description','is_recent']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'category_image', 'category_name']