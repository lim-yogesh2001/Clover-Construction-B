from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from ..models import User
from .serializers import UserDetailSerializer
from .serializers import RegisterSerializer
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken

@api_view(['GET', 'PUT'])
def user_profile(request, user_id):
    try:
        if request.method == 'GET':
            user = User.objects.get(id=user_id)
            serializer = UserDetailSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            user = User.objects.get(id=user_id)
            serializer = UserDetailSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'error': 'Something Went Wrong'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        _, token = AuthToken.objects.create(user)
        return Response({
            'user-info': {
                'id': user.id,
                'email': user.email,
            },
            'token': token
        }, status=status.HTTP_200_OK)
    return Response({"error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register_api_view(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        _, token = AuthToken.objects.create(user)

        return Response({
            'user-info': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'phone_no': user.phone_no,
                'full_name': user.full_name,
            },
            'token': token
        })
    return Response({"error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)




