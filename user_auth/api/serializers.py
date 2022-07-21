from ..models import User
from rest_framework import serializers, validators

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'full_name', 'phone_no', 'address', 'date_of_birth', 'profile_photo']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'full_name', 'phone_no', 'password']

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
            user = User.objects.create(
                username=validated_data['username'],
                email= validated_data['email'],
                full_name= validated_data['full_name'],
                phone_no= validated_data['phone_no'],
                password= validated_data['password']
            )
            return user