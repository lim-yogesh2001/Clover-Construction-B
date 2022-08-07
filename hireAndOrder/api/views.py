from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Orders, Hire, OrderTransection
from .serializer import OrderGETSerializer, OrderSerializer, HireSerializer, OrderTransectionSerializer, HirePostSerializer
from user_auth.models import User

@api_view(['GET','POST'])
def order_api(request, user_id):
    try:
        if request.method == "GET":
            user = User.objects.get(id = user_id)
            orders = Orders.objects.filter(user=user)
            serializer = OrderGETSerializer(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == "POST":
            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({"error": "Something Went Wrong"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except Orders.DoesNotExist:
        return Response({"error": "Does not Exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','DELETE', 'PUT'])
def order_detail_api(request, order_id):
    try:
        if request.method == "GET":
            order = Orders.objects.get(id= order_id)
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == "PUT":
            order = Orders.objects.get(id=order_id)
            serializer = OrderSerializer(order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Updated Successfully!!"}, status = status.HTTP_202_ACCEPTED)
            return Response({"error": "Something Went Wrong"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        elif request.method == "DELETE":
            order = Orders.objects.get(id=order_id)
            order.delete()
            return Response({"message": "Deleted Successfully"}, status= status.HTTP_404_NOT_FOUND)
        return Response({"error": "Bad request"}, status=status.HTTP_400_BAD_REQUEST)
    except Orders.DoesNotExist:
        return Response({"error":"Does not exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def order_transection_api(request):
    try:
        if request.method == "GET":
            transection = OrderTransection.objects.all()
            serializer = OrderTransectionSerializer(transection, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == "POST":
            serializer = OrderTransectionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Transection successfull!"}, status=status.HTTP_201_CREATED)
            return Response({"error": "Something Went Wrong"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response({"error": "Bad request"}, status=status.HTTP_400_BAD_REQUEST)
    except OrderTransection.DoesNotExist:
        return Response({"error":"Does not exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def order_transection_details_api(request, id):
    try:
        if request.method == "GET":
            transection = OrderTransection.objects.get(id=id)
            serializer = OrderTransectionSerializer(transection)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Something Went Wrong"}, status=status.HTTP_400_BAD_REQUEST)
    except OrderTransection.DoesNotExist:
        return Response({"error": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET','POST'])
def hire_api(request, user_id):
    try:
        if request.method == "GET":
            user = User.objects.get(id = user_id)
            hireworker = Hire.objects.filter(user_id=user)
            serializer = HireSerializer(hireworker, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == "POST":
            serializer = HirePostSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response({"error": "Something Went Wrong"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    except Hire.DoesNotExist:
        return Response({"error": "Does not Exist"}, status=status.HTTP_404_NOT_FOUND)
