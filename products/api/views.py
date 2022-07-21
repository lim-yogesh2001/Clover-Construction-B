from rest_framework import status
from rest_framework.response import Response
from ..models import Products
from stores.models import Store, Categories
from rest_framework.decorators import api_view
from .serializer import ProductSerializer

@api_view(['GET'])
def products_api(request, store_id, category_id):
    try:
        if request.method == "GET":
            store = Store.objects.get(id=store_id)
            category = Categories.objects.get(id=category_id)
            products = Products.objects.filter(store_id=store, category_id=category)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error":"Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
    except Products.DoesNotExist:
        return Response({"error": "Does Not Exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def product_detail_api(request, product_id):
    try:
        if request.method == "GET":
            product = Products.objects.get(id = product_id)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error":"Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
    except Products.DoesNotExist:
        return Response({"error": "Does Not Exist"}, status=status.HTTP_404_NOT_FOUND)
