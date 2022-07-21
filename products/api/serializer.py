from rest_framework import serializers
from ..models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'title', 'prod_image', 'description', 'brand', 'price','category_id']