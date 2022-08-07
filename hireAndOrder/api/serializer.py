from pyexpat import model
from rest_framework import serializers
from ..models import Orders, Hire, OrderTransection

class OrderGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id', 'date', 'total', 'shipping_time', 'prod_quantity','products',)
        depth = 1

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('id', 'date', 'total', 'shipping_time', 'prod_quantity','products','user',)


class HireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hire
        fields = ('id', 'worker', 'date_of_hire',)
        depth = 1

class HirePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hire
        fields = "__all__"

class OrderTransectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTransection
        fields = "__all__"


