from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.response import Response
from ..models import User
from .serializers import UserDetailSerializer
from .serializers import RegisterSerializer
from rest_framework import status, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from rest_framework.views import APIView
from .serializers import ChangePasswordSerializer

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
@permission_classes([permissions.AllowAny])
def login_view(request):
    if request.method == 'POST':
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        _, token = AuthToken.objects.create(user)
        return Response({
            'user-info': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            },
            'token': token,
        }, status=status.HTTP_200_OK)


@api_view(['POST'])
def register_api_view(request):
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
            'password': user.password,
            'full_name': user.full_name,
        },
        'token': token
    }, status=status.HTTP_201_CREATED)


class ChangePasswordView(APIView):

    # permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old password": "Wrong"}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password Updated Successfully'
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




