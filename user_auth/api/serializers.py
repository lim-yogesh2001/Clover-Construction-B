from ..models import User
from rest_framework import serializers, validators
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'full_name', 'phone_no', 'address', 'date_of_birth', 'profile_photo']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'full_name', 'phone_no', 'password',)

        extra_kwarg = {
            'password': {'write_only': True},
            'email': {
                'required': True,
                'allow_blank': False,
                'validators': [
                    validators.UniqueValidator(
                        User.objects.all(),f"That Email has already been used"
                    )
                ]
            }
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email= validated_data['email'],
            full_name= validated_data['full_name'],
            phone_no= validated_data['phone_no'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value
