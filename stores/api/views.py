from rest_framework.response import Response
from .serializer import StoreSerializer, CategorySerializer
from rest_framework.decorators import api_view
from ..models import Store, Categories
from rest_framework import status

@api_view(['GET'])
def store_list_api(request):
    try:
        if request.method == 'GET':
            store = Store.objects.all()
            serializer = StoreSerializer(store, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
    except Store.DoesNotExist:
        return Response({"error": "No Stores are available"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def store_detail_api(request, store_id):
    try:
        if request.method == 'GET':
            store = Store.objects.get(id=store_id)
            serializer = StoreSerializer(store)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
    except Store.DoesNotExist:
        return Response({"error": "No Store is available with that id"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def recent_store_api(request):
    try:
        if request.method == 'GET':
            store = Store.objects.filter(is_recent=True)
            serializer = StoreSerializer(store, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
    except Store.DoesNotExist:
        return Response({"error": "No Store is available"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def store_categories_api(request, store_id):
    try:
        if request.method == 'GET':
            store = Store.objects.get(id=store_id)
            categories = Categories.objects.filter(store_id=store)
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
    except Categories.DoesNotExist:
        return Response({"error": "No Store is available"}, status=status.HTTP_404_NOT_FOUND)