from rest_framework import status
from rest_framework.response import Response
from ..models import Worker, Department
from rest_framework.decorators import api_view
from .serializer import DepartmentSerializer, WorkerSerializer

@api_view(['GET'])
def department_list_api(request):
    try:
        if request.method == "GET":
            departments = Department.objects.all()
            serializer = DepartmentSerializer(departments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error":"Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
    except Department.DoesNotExist:
        return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def worker_list_api(request, dep_id):
    try:
        if request.method == "GET":
            department = Department.objects.get(id=dep_id)
            workers = Worker.objects.filter(departments=department)
            serializer = WorkerSerializer(workers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == "POST":
            serializer = WorkerSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
    except Department.DoesNotExist:
        return Response({"error": "Not Found"}, status= status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def woker_details_api(request, worker_id):
    try:
        if request.method == "GET":
            worker = Worker.objects.get(id = worker_id)
            serializer = WorkerSerializer(worker)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
    except Worker.DoesNotExist:
        return Response({"error": "Not Found"}, status= status.HTTP_404_NOT_FOUND)
  