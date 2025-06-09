from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from users.models import User

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','email','password','first_name','last_name','address','phone_number']

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        ref_name = 'CustomUser'
        fields = ['id','first_name','last_name','email','address','phone_number']

class SimpleUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','email','role']
        read_only_fields = ['id','first_name','email']