from rest_framework.serializers import ModelSerializer
from user.models import User

class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email']


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model=User
        fields = ['first_name', 'last_name']
        